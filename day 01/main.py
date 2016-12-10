#!/usr/bin/env python

import sys

dx = 0
dy = 0
currdir = "N"

for line in sys.stdin:
    line = line.strip()
    entries = line.split()
    for entry in entries:
        dir = entry[0]
        dist = entry[1:].split(',')[0]
        if dir == "L":
            if currdir == "N":
                currdir = "W"
            elif currdir == "E":
                currdir = "N"
            elif currdir == "S":
                currdir = "E"
            elif currdir == "W":
                currdir = "S"
        elif dir == "R":
            if currdir == "N":
                currdir= "E"
            elif currdir == "E":
                currdir= "S"
            elif currdir == "S":
                currdir= "W"
            elif currdir == "W":
                currdir= "N"
        if currdir == "N":
            dy += int(dist)
        elif currdir == "E":
            dx += int(dist)
        elif currdir == "S":
            dy -= int(dist)
        elif currdir == "W":
            dx -= int(dist)
        print ("Entry: " + dir + dist + " currdir: " + currdir + " dx, dy: " + str(dx) + " " + str(dy))

print (abs(dx) + abs(dy))
