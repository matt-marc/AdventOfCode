#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import parse as ps
import progressbar

from mpi4py import MPI

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
total_ranks = comm.Get_size()

filename = f"../inputs/day15-test-input.txt"
filename = f"../inputs/day15-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip() for line in lines]


sb_list = []
beacs = []


x_min_range = 0
x_max_range = 20
y_min_range = 0
y_max_range = 20

x_min_range = 3000000
x_max_range = 4000000
y_min_range = 3000000
y_max_range = 4000000

x_f = "Sensor at x={}, y={}: closest beacon is at x={}, y={}"
for l in lines:
    values = ps.parse(x_f, l).fixed
    sensor_pos = np.array([int(values[0]), int(values[1])])
    beacon_pos = np.array([int(values[2]), int(values[3])])

    l1_norm = np.linalg.norm(beacon_pos - sensor_pos, ord=1)

    beacs.append(beacon_pos)
    sb_list.append([sensor_pos, beacon_pos, int(l1_norm)])


def is_p_beacon(x_p):
    for b in beacs:
        if b[0] == x_p[0] and b[1] == x_p[1]:
            return True
    return False


p_vals = []


def add_to_perimiter(x, y):
    if x <= x_max_range and y <= y_max_range and x >= x_min_range and y >= y_min_range:
        pass
        p_vals.append([x, y])


def find_perimiter_list():
    for s in sb_list:
        x_s = s[0][0]
        y_s = s[0][1]

        x_max = int(s[2] + x_s)
        y_max = int(s[2] + y_s)
        x_min = int(x_s - s[2])
        y_min = int(y_s - s[2])
        # start at the top
        # move cw
        y = y_max + 1
        x = x_s
        while x <= x_max:
            add_to_perimiter(x, y)
            y = y - 1
            x = x + 1

        y = y_s
        x = x_max + 1
        while y <= y_min:
            add_to_perimiter(x, y)
            y = y - 1
            x = x - 1

        y = y_min - 1
        x = x_s
        while x >= x_min:
            add_to_perimiter(x, y)
            y = y + 1
            x = x - 1

        y = y_s
        x = x_min - 1
        while y <= y_max:
            add_to_perimiter(x, y)
            y = y + 1
            x = x + 1

    return p_vals


def count_in_row(list_pos):
    in_beacon = False

    for p in list_pos:
        x = p[0]
        y = p[1]
        x_p = np.array([x, y])

        for s in sb_list:
            sensor_pos = s[0]
            l1_sensor = s[2]

            l1_point = np.linalg.norm(x_p - sensor_pos, ord=1)
            if l1_point <= l1_sensor:
                in_beacon = True
                break

        if not in_beacon:
            print(f"found pos {x} - {y}")
            val = x * 4000000 + y
            print(f"{val=}")
            return 1
        else:
            in_beacon = False

    return 0


p_list = find_perimiter_list()
count_in_row(p_list)
# x_range = x_max - x_min
# dx = int(x_range / 4)
#
#
# if my_rank == 0:
#    print(f"compute range is ({x_min} - {x_max})")
#
#
# if my_rank == 0:
#    # print(f"running {my_rank=}")
#    x_lb = x_min
#    x_ub = x_min + dx
#    print(f"rank {my_rank} will compute values from {x_lb} to {x_ub}")
#    count_in_row(x_lb, x_ub)
# elif my_rank == 1:
#    # print(f"running {my_rank=}")
#    x_lb = x_min + dx
#    x_ub = x_min + 2 * dx
#    print(f"rank {my_rank} will compute values from {x_lb} to {x_ub}")
#    count_in_row(x_lb, x_ub)
# elif my_rank == 2:
#    # print(f"running {my_rank=}")
#    x_lb = x_min + 2 * dx
#    x_ub = x_min + 3 * dx
#    print(f"rank {my_rank} will compute values from {x_lb} to {x_ub}")
#    count_in_row(x_lb, x_ub)
# elif my_rank == 3:
#    # print(f"running {my_rank=}")
#    x_lb = x_min + 3 * dx
#    x_ub = x_max
#    print(f"rank {my_rank} will compute values from {x_lb} to {x_ub}")
#    count_in_row(x_lb, x_ub)
