#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


file = f"../inputs/day02-input.txt"

LOST_VAL = 0
DRAW_VAL = 3
WIN_VAL = 6

STATES = ["A", "B", "C"]

def get_keyval(key):
    opponent = key[0]
    me = key[2]
    me_conv = chr(ord(me) - 23)
    shape_val = int(ord(me_conv) - 64)

    if opponent == me_conv:
        return DRAW_VAL + shape_val

    win_state = STATES[shape_val-2]
    if win_state == opponent:
        return WIN_VAL + shape_val

    return LOST_VAL + shape_val


def parse_input(filename):
    file = open(filename, "r")
    lines = file.readlines()
    lines[:] = [line.strip() for line in lines]
    return lines


input_list = parse_input(file)
total = 0
for r in input_list:
    total += get_keyval(r)
print(total)
