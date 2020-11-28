#!/usr/bin/env bash

targetUrl='https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png'
filename='pico_img.png'
wget -O ${filename} ${targetUrl}
echo "Flag: $(strings -n9 ${filename} | grep -oP 'picoCTF{.*?}')"
