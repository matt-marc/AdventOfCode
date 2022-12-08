#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"../inputs/day01-input.txt"

file = open(filename, 'r')
lines = file.readlines()


cals = 0
elf = 1
max_cals = 0
max_elf = 0


for line in lines:
    if line == "\n":

        if cals > max_cals:
            max_cals = cals
            max_elf = elf
        elf += 1
        cals = 0
    else:
        cals += int(line.strip())

print(f"{max_elf=} {max_cals=}")


