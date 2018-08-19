#!/usr/bin/env python3
origin, encrypt, lineTo, lineBack = [input() for _ in range(4)]
to = dict(zip(origin, encrypt))
back = dict(zip(encrypt, origin))
for sym in lineTo:
    print(to[sym], end='')
print()
for sym in lineBack:
    print(back[sym], end='')