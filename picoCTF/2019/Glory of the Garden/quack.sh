#!/usr/bin/env bash

targetUrl='https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg'
filename='garden.jpg'
wget -O ${filename} ${targetUrl}
echo "Flag: $(strings -n9 ${filename} | grep -oP 'picoCTF{.*?}')"
