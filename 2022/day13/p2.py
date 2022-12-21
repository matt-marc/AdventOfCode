#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import functools
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
        return -1

    print("E yes: left side ran out ")
    return -1




div_pk1 = [[2]]
div_pk2 = [[6]]
evals.append(div_pk1)
evals.append(div_pk2)

sort_l = sorted(evals, key=functools.cmp_to_key(compare_list))
print(sort_l)

idx_1 = sort_l.index(div_pk1) + 1
idx_2 = sort_l.index(div_pk2) + 1
print(idx_1)
print(idx_2)
print(idx_1*idx_2)
