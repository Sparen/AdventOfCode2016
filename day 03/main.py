#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    sides = line.split()
    v1 = int(sides[0])
    v2 = int(sides[1])
    v3 = int(sides[2])

    if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:
        count += 1

print(count)
