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

    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
        count += 1
    elif(elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
        count += 1

    #print(f"{elf1=}")
    #print(f"{elf2=}")
    #print(f"{count=}")
    #input()

print(count)


