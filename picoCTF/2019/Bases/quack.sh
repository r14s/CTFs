#!/usr/bin/env bash

chall_str='bDNhcm5fdGgzX3IwcDM1'
echo "Flag: picoCTF{$(base64 -d <<< "$chall_str")}"
