#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"../inputs/day04-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip().split(",") for line in lines]

count = 0
for row in range(len(lines)):
    line = lines[row]

    elf1 = list(map(int,(line[0].split("-"))))
    elf2 = list(map(int,(line[1].split("-"))))


    left_val = max(elf1[0] ,elf2[0])
    right_val = min(elf1[1],elf2[1])

    if (left_val <= right_val):
        count += 1

print(count)


