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


total = lines[0]
for line in lines[1:]:
    total = [sum(i) for i in zip(total, line)]


gamma = 0
epsilon = 0
mid = len(lines)/2

for v in total:
    if v > mid:
        gamma = (gamma << 1) | 1
        epsilon = (epsilon << 1) | 0
    else:
        gamma = (gamma << 1) | 0
        epsilon = (epsilon << 1) | 1

print(gamma*epsilon)
