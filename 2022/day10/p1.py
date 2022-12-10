#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt

filename = f"../inputs/day10-input.txt"
#filename = f"../inputs/day10-test-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip().split() for line in lines]


eax = 1
buffer = [0, 0]
i = 0
cycles = 220
stop_cycles = [20, 60, 100, 140, 180, 220]
total = 0

for c in range(cycles+1):
    print(f"starting cycle {c+1}")
    print(f"EAX = {eax}")

    if c+1 in stop_cycles:
        print("at stop cycle")
        total += eax * (c+1)
        #input()

    # check if pending instruction to compute
    if buffer[0] == 0:
        # nothing pending
        print("no pending instructions")
        # clear buffer
        print(f"{buffer=} and {eax=}")
        l = lines[i]
        if len(l) > 1:
            buffer[0] = 1
            buffer[1] = int(l[1])
            print(f"adding instruction {l} to buffer")
            i += 1
        else:
            print("noop")
            buffer[0] = 0
            buffer[1] = 0
            i += 1
        # ready for next instruction
    else:
        # still computing
        print("still computing")
        print(f"{buffer=}")
        buffer[0] = buffer[0] - 1
        print(f"{buffer=}")

    if buffer[0] == 0:
        eax += buffer[1]


    print(f"end cycle {c+1}")
    print(f"EAX = {eax}")
    print("\n\n")


print(total)
