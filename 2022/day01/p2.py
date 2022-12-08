#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import bisect


filename = f"../inputs/day01-input.txt"

file = open(filename, "r")
lines = file.readlines()


cals = 0
top_3 = [0, 0, 0]

for line in lines:
    if line == "\n":
        if cals > top_3[0]:
            bisect.insort(top_3, cals)
            top_3.pop(0)
        cals = 0
    else:
        cals += int(line.strip())


print(f"top_3 = {top_3}")
print(sum(top_3))
