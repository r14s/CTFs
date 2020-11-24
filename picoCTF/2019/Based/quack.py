#!/usr/bin/env python3

import socket
import re

targetAddr = 'jupiter.challenges.picoctf.org'
targetPort = 29956

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((targetAddr, targetPort))

dataRegex = b'Please give (?:me )?the (.*) as a word.'
msgEnd = b'Input:\n'

binary = lambda s: ''.join([chr(int(w, 2)) for w in s.split()])
octal =  lambda s: ''.join([chr(int(w, 8)) for w in s.split()])
hex =    lambda s: bytes.fromhex(s).decode()
challHandler = { 0: binary, 1: octal, 2: hex }

chunksize = 1024
msg = b''
msgNumber = 0
while True:
    chunk = sock.recv(chunksize)
    if not len(chunk):
        break
    print(chunk.decode())
    msg += chunk
    if msg.endswith(msgEnd):
        chall = re.search(dataRegex, msg).group(1).decode()
        answer = ''.join([challHandler[msgNumber](chall),'\n']).encode('utf-8')
        print(f'Sending {answer}')
        sock.sendall(answer)
        msgNumber += 1
        msg = b''
