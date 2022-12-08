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
            return False
    print("top clear")
    return True


def clear_bot(x, y, t):
    for c_y in range(y, y_len, 1):
        c_t = lines[c_y + 1][x]
        if c_t >= t:
            return False
    print("bottom clear")
    return True


def clear_left(x, y, t):
    for c_x in range(x, 0, -1):
        c_t = lines[y][c_x - 1]
        print(f"comparing {c_t} with tree {t}")
        if c_t >= t:
            return False

    print("left clear")
    return True


def clear_right(x, y, t):
    for c_x in range(x, x_len, 1):
        c_t = lines[y][c_x + 1]
        if c_t >= t:
            return False

    print("right clear")
    return True


total = 0
for y in range(1, y_len):
    for x in range(1, x_len):
        tree_val = lines[y][x]
        print(f"\n\nCOMP pos ({x},{y}) = {tree_val}")
        fy = clear_bot(x, y, tree_val) or clear_top(x, y, tree_val)
        fx = clear_left(x, y, tree_val) or clear_right(x, y, tree_val)
        print(f"\n\n")

        if fy or fx:
            print(f"clear tree at pos ({x},{y}) = {tree_val}")
            print(f"\n\n")
            total += 1
            # input()


print(f"{x_len=}")
print(f"{y_len=}")
per = x_len * 4
print(total + per)
