#!/usr/bin/env python3

import requests
import re
from os import path
from bitstring import Bits

targetUrl = 'https://jupiter.challenges.picoctf.org/static/95be9526e162185c741259a75dffa0ab/whitepages.txt'
targetFilename = 'whitepages.txt'

if not path.exists(targetFilename):
    with open(targetFilename, 'xb') as f:
        r = requests.get(targetUrl)
        f.write(r.content)

with open(targetFilename, 'r') as f:
    fileContent = f.read()

uniqueChars = ''.join(sorted(set(fileContent)))
mapping = {ch: i for ch,i in zip(uniqueChars, reversed(range(2)))}
bits = []
for ch in fileContent:
    bits.append(mapping[ch])
message = Bits(bits).tobytes().decode()
flag = re.search('picoCTF{.*?}', message)[0]
print(f"Flag: {flag}")
