#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"../inputs/day06-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip() for line in lines]


SIZE = 4

def is_unique(l):
    leng = len(set(l))
    return leng == len(l)



line = lines[0]

working_bits = line[0:SIZE]

unique_f = is_unique(list(working_bits))

for bit in range(SIZE, len(line)):
    new_bit = line[bit]

    if new_bit in working_bits or not unique_f:
        working_bits = working_bits + new_bit
        working_bits = working_bits[1:]
        unique_f = is_unique(list(working_bits))

    if(unique_f):
        print(f"{bit+1=}")
        input()







