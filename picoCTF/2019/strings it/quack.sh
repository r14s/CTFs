#!/usr/bin/env bash

targetURL='https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings'
echo "Flag: $(wget -q -O - "$targetURL" | strings -n9 | grep -m1 picoCTF)"
