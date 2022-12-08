#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"../inputs/day03-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [list(line.strip()) for line in lines]


def get_prio(item):
    val = int(ord(item))
    if val >= 97:
        val = val - 96
    else:
        val = val - 64 + 26
    return val


total_val = 0

for row in range(0, len(lines), 3):
    c1 = lines[row]
    c2 = lines[row + 1]
    c3 = lines[row + 2]

    for i in c1:
        if i in c2:
            if i in c3:
                total_val += get_prio(i)
                break

print(total_val)


