#!/bin/bash
# usage: render.sh input.html output.pdf  (fails unless exactly 1 page)
set -e
in="$1"; out="$2"
[ -z "$in" ] || [ -z "$out" ] && { echo "usage: render.sh in.html out.pdf"; exit 2; }
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --no-pdf-header-footer --print-to-pdf="$out" "file://$(cd "$(dirname "$in")" && pwd)/$(basename "$in")" >/dev/null 2>&1
n=$(pdfinfo "$out" | awk '/^Pages:/{print $2}')
echo "pages: $n"
[ "$n" = "1" ] || { echo "FAIL: expected 1 page"; exit 1; }
