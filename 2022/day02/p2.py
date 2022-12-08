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
POINTS = [1, 2 ,3] #has to be a python way to do this

def get_keyval(key):
    opponent = key[0]
    me = key[2]

    opp_index = int(ord(opponent) - 65)

    # X = -1
    # Y =  0
    # Z = +1

    if me == "Y":
        return DRAW_VAL + opp_index + 1
    if me == "X":
        return LOST_VAL + POINTS[opp_index - 1]
    if me == "Z":
        return WIN_VAL + POINTS[(opp_index + 1)%3]

def parse_input(filename):
    file = open(filename, "r")
    lines = file.readlines()
    lines[:] = [line.strip() for line in lines]
    return lines


input_list = parse_input(file)
total = 0
#get_keyval("A X")
#get_keyval("A Y")
#get_keyval("A Z")
for r in input_list:
    total += get_keyval(r)
print(total)
