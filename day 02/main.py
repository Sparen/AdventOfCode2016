#!/usr/bin/env python

import sys

for line in sys.stdin:
    currkey = 5
    for input in line:
        if input == "D" and currkey < 6:
            currkey += 3
        elif input == "U" and currkey > 3:
            currkey -= 3
        elif input == "L" and currkey % 3 != 1:
            currkey -= 1
        elif input == "R" and currkey % 3 != 0:
            currkey += 1
    print currkey

