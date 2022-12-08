#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"inputs/day03-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [list(map(int, line.strip())) for line in lines]

running_avg = lines[0]


for i in range(1, len(lines)):
    line = lines[i]
    mid_val = i / 2
    for j in range(len(line)):
        bit = line[j]
        avg = running_avg[j]

        if bit + avg > mid_val:
            running_avg[j] += 1
        else:
            running_avg[j] += 0

print(running_avg)
# total = [sum(i) for i in zip(total, line)]
# for i in zip(total, line):
#     print(i)
#     total = sum(i)


# gamma = 0
# epsilon = 0
#
# for v in total:
#    if v > mid:
#        gamma = (gamma << 1) | 1
#        epsilon = (epsilon << 1) | 0
#    else:
#        gamma = (gamma << 1) | 0
#        epsilon = (epsilon << 1) | 1
#
# print(gamma*epsilon)
