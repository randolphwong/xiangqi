#!/usr/bin/env python3

import re
import os

with open('../chess.html', 'rb') as f:
    data = f.read()

data = bytes(i for i in data if i < 128)
data = data.decode('ascii')
res = re.findall(r'images/[^.]+.gif', data)

for i in res:
    # print('http://www.springfrog.com/games/chess/chinese/' + i)
    os.system('wget http://www.springfrog.com/games/chess/chinese/' + i)
