#!/bin/bash
# Tiny Shakespeare dataset'ini indir
set -e

URL="https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
OUTPUT="dataset.txt"

if [ ! -f "$OUTPUT" ]; then
    echo "İndiriliyor: $URL"
    wget -q "$URL" -O "$OUTPUT"
    echo "Kaydedildi: $OUTPUT ($(wc -c < "$OUTPUT") bytes)"
else
    echo "$OUTPUT zaten var ($(wc -c < "$OUTPUT") bytes)"
fi
