#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


filename = f"../inputs/day05-input.txt"

file = open(filename, "r")
linesop = file.readlines()
linesop[:] = [list(line) for line in linesop[1:9]]



new_stack = []
for l in linesop:
    new_l = l[1::4]
    new_stack.append(new_l)

stacks = []
for i in zip(*new_stack):
    new_l = list(i)
    new_l = [ i for i in new_l if i != " "]
    stacks.append(list(new_l[::-1]))

print(stacks)
