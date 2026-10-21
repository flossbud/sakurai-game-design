#!/bin/bash
# OCR the burned-in English subtitles of every downloaded episode (skips ones already done).
# usage: tools/run_ocr.sh <work_dir> <python-with-rapidocr>
#   python env: uv venv .venv && uv pip install rapidocr onnxruntime numpy
T=$(cd "$(dirname "$0")" && pwd); D=${1:?work dir}; PY=${2:?python}
mkdir -p "$D/ocr"
for v in "$D"/video/*.mp4; do id=$(basename "$v" .mp4); [ -s "$D/ocr/$id.json" ] || echo "$v"; done \
  | xargs -P 3 -I{} sh -c 'id=$(basename "{}" .mp4); "'"$PY"'" -I "'"$T"'/ocr_subs.py" "{}" "'"$D"'/ocr/$id.json"'
