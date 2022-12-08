#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt

filename = f"../inputs/day08-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [list(map(int, line.strip())) for line in lines]


y_len = len(lines) - 1
x_len = len(lines[0]) - 1

print(f"{x_len=}")
print(f"{y_len=}")


print(f"{lines[0][x_len-1]=}")


def clear_top(x, y, t):
    for c_y in range(y, 0, -1):
        c_t = lines[c_y - 1][x]
        if c_t >= t:
            return y - c_y + 1
    print("top clear")
    return y


def clear_bot(x, y, t):
    for c_y in range(y, y_len, 1):
        c_t = lines[c_y + 1][x]
        if c_t >= t:
            return c_y - y + 1
    print("bottom clear")
    return y_len - y


def clear_left(x, y, t):
    for c_x in range(x, 0, -1):
        c_t = lines[y][c_x - 1]
        if c_t >= t:
            return x - c_x + 1
    print("left clear")
    return x


def clear_right(x, y, t):
    for c_x in range(x, x_len, 1):
        c_t = lines[y][c_x + 1]
        if c_t >= t:
            return c_x - x + 1

    print("right clear")
    return x_len - x


total = 0
for y in range(1, y_len):
    for x in range(1, x_len):
        tree_val = lines[y][x]
        print(f"\n\nCOMP pos ({x},{y}) = {tree_val}")
        f_bot = clear_bot(x, y, tree_val)
        f_top = clear_top(x, y, tree_val)
        f_left = clear_left(x, y, tree_val)
        f_right = clear_right(x, y, tree_val)
        points = f_top * f_bot * f_left * f_right
        print(f"{f_bot=}")
        print(f"{f_top=}")
        print(f"{f_left=}")
        print(f"{f_right=}")
        print(f"{points=}")
        print(f"\n\n")

        if points > total:
            total = points

print(total)
