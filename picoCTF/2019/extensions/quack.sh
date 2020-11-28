#!/usr/bin/env bash

# You can open the file with image viewer like a normal person and read the flag, or...
targetUrl='https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt'
filename='flag.txt'
wget -O ${filename} ${targetUrl}
echo "Flag: $(tesseract flag.txt - -l eng)"
