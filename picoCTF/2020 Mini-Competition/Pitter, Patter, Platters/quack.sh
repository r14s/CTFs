#!/usr/bin/env bash

targetUrl='https://jupiter.challenges.picoctf.org/static/ca14d110858381cb297c1d22d62391a3/suspicious.dd.sda1'
fileName='suspicious.dd.sda1'
wget -O ${fileName} ${targetUrl}
suspicious_filename='suspicious-file.txt'
metadata_address=$(fls ${fileName} | grep ${suspicious_filename} | awk '{ print substr($2,1,length($2)-1) }')
solution=$(icat -s -h ${fileName} ${metadata_address} | tr -d '\0' | tail -n1 | rev)
echo "Flag: ${solution}"
