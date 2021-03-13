#!/usr/bin/env python
# coding: utf-8

from collections import Counter

MODS = ['BckSp','End','Home','Enter','Tab','Up','Esc','Down','Left','Right','Ins','Del','PgUp','CpsLk','PgDn','AltGr','LMeta','LAlt','LCtrl','LShft','RShft']

with open('/var/log/logkeys.log') as f:
    a=f.readlines()[2:]

keys = ''.join([d for l in a for d in l.split(' > ') if '2021' not in d])
k=[s for k in keys.split('<') for s in k.split('>') if len(s) > 0]
mods = [x for x in k if x in MODS]
rest = [x for x in k if x not in MODS]
chars = ''.join([x for x in rest if not x.startswith('#+')])

all = Counter(mods) + Counter(chars)
sorted(all.items(), key=lambda x: x[1], reverse=True)
