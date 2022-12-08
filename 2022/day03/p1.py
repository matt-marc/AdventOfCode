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

for row in range(len(lines)):
    items = lines[row]
    size = int(len(items)/2)
    c1 = items[:size]
    c2 = items[size:]

    for i in c1:
        if i in c2:
            total_val += get_prio(i)
            break


print(total_val)


