#!/usr/bin/env python3

import os

sound = ['illegal', 'loss', 'win', 'draw', 'check2', 'check', 'capture2', 'capture', 'move2', 'move', 'click', 'newgame']

for i in sound:
    os.system('wget http://www.springfrog.com/games/chess/chinese/sounds/' + i + '.wav')
