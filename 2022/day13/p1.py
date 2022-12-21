#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import parse
import ast

filename = f"../inputs/day13-test-input.txt"
filename = f"../inputs/day13-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip() for line in lines]


evals = []
for l_string in lines:
    if not l_string == "":
        evals.append(ast.literal_eval(l_string))


def premote_to_list(a, b):
    if type(a) == type(1):
        return [[a], b]
    if type(b) == type(1):
        return [a, [b]]


def compare_list(a, b):
    # start over each item
    for i, c in enumerate(a):
        a_i = c

        # check if the current index outnumbers
        # the right list
        if len(b) == i:
            print("E no: right side ran out")
            return 1

        b_i = b[i]

        print(f"will being comparing {a_i=} to {b_i=}")
        if type(a_i) == type(b_i):
            print("comparing same type")
            if type(a_i) == type([]):
                print("comparing 2 sub lists")

                ret = compare_list(a_i, b_i)
                if not ret == 0:
                    return ret

            if a_i > b_i:
                print("E no: left side bigger than right")
                return 1
            elif a_i < b_i:
                print("E yes: left smaller than right")
                return -1
            else:
                print("same")
                pass

        else:
            print("not same type")
            new_items = premote_to_list(a_i, b_i)
            a_i = new_items[0]
            b_i = new_items[1]
            ret = compare_list(a_i, b_i)

            if not ret == 0:
                return ret


    if len(a) == len(b):
        print("same list length")
        return 0

    print("E yes: left side ran out ")
    return -1

def val_lists(a, b):
    for i, c in enumerate(a):
        a_i = c

        if len(b) == i:
            print("E no: right list ran out")
            return i

        b_i = b[i]

        print(f"will being comparing {a_i=} to {b_i=}")
        if type(a_i) == type(b_i):
            print("comparing same type")
        else:
            print("not same type")
            new_items = premote_to_list(a_i, b_i)
            a_i = new_items[0]
            b_i = new_items[1]



t_sum = 0
for i in range(0, len(evals) - 1, 2):
    left_e = evals[i]
    right_e = evals[i + 1]
    lvl = int(i/2) + 1
    print(f"evaluation {lvl} {left_e} vs {right_e}")
    ret = compare_list(left_e, right_e)
    if ret == -1:
        t_sum += lvl


print(f"total sum is {t_sum}")
