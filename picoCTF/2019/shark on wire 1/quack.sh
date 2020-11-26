#!/usr/bin/env bash

targetUrl='https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap'
filename='capture.pcap'
wget -O ${filename} ${targetUrl}
echo "Flag: $(while read n; do echo -en "\x${n}"; done < <(tshark -r ${filename} -T fields -e data 'udp.stream eq 6'))"
