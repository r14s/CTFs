#!/usr/bin/env bash

targetAddr='jupiter.challenges.picoctf.org'
targetPort=4427
echo "Flag: $(grep -m1 picoCTF <(ncat "$targetAddr" "$targetPort" --recv-only 2> /dev/null))"
