#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"inputs/day01-input.txt"

data = pd.read_csv(filename, header=None, names=["Depths"])

d = data["Depths"].to_numpy()

count = 0

for i in range(1, len(d), 1):
    #print(f"val {i} is {d[i]}")
    prev = d[i-1]
    val = d[i]
    if val > prev:
        count = count + 1



print (f"final val is {count}")
