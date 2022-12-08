#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"../inputs/day05-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip().split(" ") for line in lines[10:]]

file = open(filename, "r")
linesop = file.readlines()
linesop[:] = [list(line.strip()) for line in linesop[1:9]]

idx_val = list(range(1,9*4, 4))
print(idx_val)

for l in linesop:
    l += [' '] *(35-len(l))

stacks = []
for col in idx_val:
    col_stack = []
    for l in linesop:
        val = l[col]
        if not val == " ":
            col_stack.insert(0,val)

    stacks.append(col_stack)



#print(linesop)




for move in range(len(lines)):
    number_moves = int(lines[move][1])
    from_idx = int(lines[move][3])
    to_idx = int(lines[move][5])

    print(f"moving {number_moves} boxs to {to_idx} from {from_idx}")

    for i in range(number_moves):
        if len(stacks[from_idx - 1]) > 0:
            val = stacks[from_idx - 1].pop()
            print(f"moving{val}")
            stacks[to_idx - 1].append(val)

    print(stacks)
    #input()


for s in stacks:
    print(s[-1])
