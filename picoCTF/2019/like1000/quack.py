#!/usr/bin/env python3

from os import path
import requests
import tarfile
from io import BytesIO

targetUrl = 'https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar'
targetFilename = '1000.tar'

if not path.exists(targetFilename):
    with open(targetFilename, 'xb') as f:
        r = requests.get(targetUrl)
        f.write(r.content)

with open(targetFilename, 'rb') as f:
    current_archive = BytesIO(f.read())

while True:
    with tarfile.open(fileobj = current_archive) as archive:
        for file in archive.getnames():
            if file.endswith('.tar'):
                print(f"Processing: {file}")
                current_archive = BytesIO(archive.extractfile(file).read())
                break
        else:
            print("Last archive extracted to current directory")
            archive.extractall()
            break
