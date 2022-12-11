#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np

filename = f"../inputs/day10-input.txt"
#filename = f"../inputs/day10-test-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip().split() for line in lines]


eax = 1
buffer = [0, 0]
i = 0
cycles = 239
printline = ""
stop_cycles = [1, 41, 81, 121, 161, 201]
crt_val = 0
black_square = f"\U0000FFED"

for c in range(cycles+1):
    crt_val = (c) % 40
    print(f"starting cycle {c+1}")
    print(f"EAX = {eax}")
    print(f"CRT = {crt_val}")

    if c+1 in stop_cycles:
        print("at stop cycle")
        printline = printline + "\n"

    if crt_val >= (eax-1) and  crt_val <= (eax + 1):
        printline = printline + black_square
        #printline = printline + "#"
    else:
        printline = printline + " "

    # check if pending instruction to compute
    if buffer[0] == 0:
        l = lines[i]
        if len(l) > 1:
            buffer[0] = 1
            buffer[1] = int(l[1])
            i += 1
        else:
            buffer[0] = 0
            buffer[1] = 0
            i += 1
        # ready for next instruction
    else:
        # still computing
        buffer[0] = buffer[0] - 1

    if buffer[0] == 0:
        eax += buffer[1]

    print(f"end cycle {c+1}")
    print(f"EAX = {eax}")
    print("\n\n")


print(printline)

