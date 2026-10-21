"""OCR the burned-in English subtitle bar from a Sakurai episode.

usage: python -I ocr_subs.py <video.mp4> <out.json>

Samples the bottom strip at SAMPLE_FPS, splits it into stable segments by
comparing binarized text masks, OCRs the middle frame of each segment and
writes [{start, end, text}] to out.json.
"""
import json
import subprocess
import sys

import numpy as np

SAMPLE_FPS = 4
W, H = 1280, 720
STRIP_Y0 = 612  # subtitle bar starts ~615 at 720p
STRIP_H = H - STRIP_Y0
TEXT_THRESH = 190  # white text on dark gray bar
MIN_TEXT_PX = 400  # fewer white pixels than this = no subtitle
CHANGE_FRAC = 0.12  # mask XOR / union above this = new line


def probe_size(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height", "-of", "csv=p=0", path], text=True)
    w, h = out.strip().split("\n")[0].split(",")
    return int(w), int(h)


def strips(path):
    w, h = probe_size(path)
    vf = f"scale={W}:{H},crop={W}:{STRIP_H}:0:{STRIP_Y0},fps={SAMPLE_FPS},format=gray"
    proc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-i", path, "-vf", vf, "-f", "rawvideo", "-"],
        stdout=subprocess.PIPE)
    size = W * STRIP_H
    i = 0
    while True:
        buf = proc.stdout.read(size)
        if len(buf) < size:
            break
        yield i / SAMPLE_FPS, np.frombuffer(buf, np.uint8).reshape(STRIP_H, W)
        i += 1
    proc.wait()


def has_bar(gray):
    # the subtitle bar is a flat dark gray; check the darker 70% of pixels
    dark = np.percentile(gray, 70)
    return dark < 90


def segments(path):
    segs = []
    cur = None
    for t, g in strips(path):
        mask = g > TEXT_THRESH
        n = int(mask.sum())
        if not has_bar(g) or n < MIN_TEXT_PX:
            if cur:
                segs.append(cur)
                cur = None
            continue
        if cur is not None:
            union = np.logical_or(mask, cur["mask"]).sum()
            diff = np.logical_xor(mask, cur["mask"]).sum() / max(union, 1)
            if diff < CHANGE_FRAC:
                cur["end"] = t
                cur["frames"].append(g)
                continue
            segs.append(cur)
        cur = {"start": t, "end": t, "mask": mask, "frames": [g]}
    if cur:
        segs.append(cur)
    return segs


def line_crops(g):
    """Split the strip into text lines by row projection of the text mask."""
    mask = g > TEXT_THRESH
    rows = mask.sum(axis=1) > 2
    bands, start = [], None
    for y, on in enumerate(list(rows) + [False]):
        if on and start is None:
            start = y
        elif not on and start is not None:
            if y - start >= 8:
                bands.append((start, y))
            start = None
    crops = []
    for y0, y1 in bands:
        cols = np.where(mask[y0:y1].any(axis=0))[0]
        x0, x1 = max(cols[0] - 12, 0), min(cols[-1] + 12, W)
        y0, y1 = max(y0 - 8, 0), min(y1 + 8, STRIP_H)
        crop = 255 - g[y0:y1, x0:x1]  # dark text on light background
        crops.append(np.ascontiguousarray(np.stack([crop] * 3, axis=-1)))
    return crops


def main():
    from rapidocr import RapidOCR

    video, out = sys.argv[1], sys.argv[2]
    engine = RapidOCR()
    lines = []
    for s in segments(video):
        if len(s["frames"]) < 2:
            continue  # fade-in/out transition frame
        g = s["frames"][len(s["frames"]) // 2]
        parts = []
        for crop in line_crops(g):
            res = engine(crop, use_det=False, use_cls=False, use_rec=True)
            parts += [t.strip() for t in (res.txts or []) if t.strip()]
        text = " ".join(parts).strip()
        if not text:
            continue
        if lines and lines[-1]["text"] == text:
            lines[-1]["end"] = s["end"]
            continue
        lines.append({"start": round(s["start"], 2), "end": round(s["end"] + 1 / SAMPLE_FPS, 2), "text": text})
    with open(out, "w") as f:
        json.dump(lines, f, ensure_ascii=False, indent=0)
    print(f"{video}: {len(lines)} lines")


if __name__ == "__main__":
    main()
