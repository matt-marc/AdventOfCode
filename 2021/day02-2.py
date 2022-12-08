#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"inputs/day02-input.txt"

data = pd.read_csv(filename, header=None, names=["Dir", "Value"],sep=" ")

direction = data["Dir"]
value = data["Value"]


fwd = 0
aim = 0
depth = 0

# has to be a better way?
for i in range(len(direction)):
    d = direction[i]
    v = value[i]

    if d == "forward":
        fwd = fwd + v
        depth = depth + aim * v

    elif d == "down":
        aim = aim + v

    elif d == "up":
        aim = aim - v



fv = depth*fwd

print(f"final val is {fv}")



