#!/bin/bash
# Download every episode of "Masahiro Sakurai on Creating Games" (English channel) at 720p, video only.
# usage: tools/fetch_videos.sh <work_dir>    (needs yt-dlp and node; ~8 GB)
set -e
D=${1:?work dir}; mkdir -p "$D/video"; cd "$D"
yt-dlp --flat-playlist --print "%(id)s	%(title)s	%(duration)s" \
  "https://www.youtube.com/@sora_sakurai_en/videos" > videos.tsv
grep -v Compilation videos.tsv | cut -f1 | sed 's|^|https://www.youtube.com/watch?v=|' > urls.txt
split -n r/3 -d urls.txt part_
for p in part_0*; do
  yt-dlp --js-runtimes node -i --no-abort-on-error \
    -f "298/bv*[height<=720][ext=mp4]/bv*[height<=720]" \
    -o "video/%(id)s.%(ext)s" --download-archive "archive_$p.txt" \
    --sleep-requests 1 -a "$p" > "dl_$p.log" 2>&1 &
done
wait
