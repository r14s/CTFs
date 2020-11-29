#!/usr/bin/env bash

targetUrl='https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap'
filename='capture.pcap'
wget -q -O ${filename} ${targetUrl}
# NOTE: "start", ["whatever"]..., "end" payloads are all on udp.dstport 22
# ALSO: udp.srcport are ASCII values
echo -e "Flag: $(tshark -r ${filename} -T fields -e 'udp.srcport' 'udp.dstport eq 22' | awk '{gsub(/^.0*/ ,"", $1); printf "\\%04o", $1 }')"
