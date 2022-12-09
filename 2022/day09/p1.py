#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt

filename = f"../inputs/day09-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip().split() for line in lines]


x = 0
y = 0
head = [[x, y]]

for line in lines:
    direction = line[0]
    spaces = int(line[1])

    for delta in range(spaces):
        if direction == "U":
            y += 1
        elif direction == "D":
            y -= 1
        elif direction == "R":
            x += 1
        elif direction == "L":
            x -= 1

        head.append([x, y])


def tail_pos(p1, p2, tail_p):
    px1 = p1[0]
    py1 = p1[1]
    px2 = p2[0]
    py2 = p2[1]

    h_delta_x1 = abs(px1 - tail_p[0])
    h_delta_y1 = abs(py1 - tail_p[1])
    h_delta_x2 = abs(px2 - tail_p[0])
    h_delta_y2 = abs(py2 - tail_p[1])

    print(f"head moved from {p1} -> {p2}")
    if h_delta_x2 > 1:
        # print(f"head moved away from tail x dir")
        return [px1, py1]
    elif h_delta_y2 > 1:
        # print(f"head moved away from tail y dir")
        return [px1, py1]
    else:
        return tail_p


tail = [[0, 0]]
for i in range(len(head) - 1):
    new_tail = tail_pos(head[i], head[i + 1], tail[i])
    tail.append(new_tail)

nparr = np.array(tail)
unique_tail = np.unique(nparr, axis=0)
print(len(unique_tail))
