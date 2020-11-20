#!/usr/bin/env bash

targetUrl='https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file'
echo "Flag: $(wget -O - -q "$targetUrl" | grep -m1 picoCTF)"
