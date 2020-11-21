#!/usr/bin/env python3

targetAddr='jupiter.challenges.picoctf.org'
targetPort=41120
echo "Flag: $(ncat "$targetAddr" "$targetPort" --recv-only | grep -m1 picoCTF)"
