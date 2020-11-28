#!/usr/bin/env python3

from PIL import Image
from bitstring import Bits
import requests

# Download target image
targetUrl = 'https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png'
targetFilename = 'buildings.png'
with open(targetFilename, 'xb') as f:
    r = requests.get(targetUrl)
    f.write(r.content)

# Extract lsb bits
with Image.open(targetFilename, 'r') as img:
    imgData = img.getdata()
rgbBytes = [byte for pixel in imgData for byte in pixel[:3]]
lsbBits = [byte & 1 for byte in rgbBytes]

# Decode message from bits, also remove null bytes for aesthetics
message = Bits(lsbBits)
nullPos = message.find('0b00000000', bytealigned=True)[0]
decodedMessage = message[:nullPos].tobytes().decode()
print(f"Flag: {decodedMessage}")
