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

x_min = -7
x_max = 10
y_scan = 10
x_min = -700000
x_max = 100000
y_scan = 2000000

x_f = "Sensor at x={}, y={}: closest beacon is at x={}, y={}"
for l in lines:
    values = ps.parse(x_f, l).fixed
    sensor_pos = np.array([int(values[0]), int(values[1])])
    beacon_pos = np.array([int(values[2]), int(values[3])])

    x_max = max(int(values[0]), int(values[2]), x_max)
    x_min = min(int(values[0]), int(values[2]), x_min)

    l1_norm = np.linalg.norm(beacon_pos - sensor_pos, ord=1)

    beacs.append(beacon_pos)
    sb_list.append([sensor_pos, beacon_pos, int(l1_norm)])


def is_p_beacon(x_p):
    for b in beacs:
        if b[0] == x_p[0] and b[1] == x_p[1]:
            return True
    return False

def count_in_row(x_lb, x_ub):
    count = 0
    for x in range(x_lb, x_ub):
        x_p = np.array([x, y_scan])

        for s in sb_list:
            sensor_pos = s[0]
            l1_sensor = s[2]
            l1_point = np.linalg.norm(x_p - sensor_pos, ord=1)
            # print(f"checking point with sensor {sensor_pos}")
            # print(f"l1 beacon {l1_sensor} l1 point{l1_point}")
            if l1_point <= l1_sensor:
                #count += 1
                if is_p_beacon(x_p):
                    print(f"beacon on line {x_p}")
                    #count += 1
                else:
                    count += 1
                break

    return count


x_max = int(x_max * 1.5)
x_min = int(x_min * 4.0)
x_range = x_max - x_min
dx = int(x_range / 4)


if my_rank == 0:
    print(f"compute range is ({x_min} - {x_max})")


sum_for_section = np.zeros(1)
mpi_sum = np.zeros(1)
if my_rank == 0:
    # print(f"running {my_rank=}")
    x_lb = x_min
    x_ub = x_min + dx
    print(f"rank {my_rank} will compute values from {x_lb} to {x_ub}")
    sum_for_section[0] = count_in_row(x_lb, x_ub)
elif my_rank == 1:
    # print(f"running {my_rank=}")
    x_lb = x_min + dx
    x_ub = x_min + 2 * dx
    print(f"rank {my_rank} will compute values from {x_lb} to {x_ub}")
    sum_for_section[0] = count_in_row(x_lb, x_ub)
elif my_rank == 2:
    # print(f"running {my_rank=}")
    x_lb = x_min + 2 * dx
    x_ub = x_min + 3 * dx
    print(f"rank {my_rank} will compute values from {x_lb} to {x_ub}")
    sum_for_section[0] = count_in_row(x_lb, x_ub)
elif my_rank == 3:
    # print(f"running {my_rank=}")
    x_lb = x_min + 3 * dx
    x_ub = x_max
    print(f"rank {my_rank} will compute values from {x_lb} to {x_ub}")
    sum_for_section[0] = count_in_row(x_lb, x_ub)

print(f"{my_rank} has value {sum_for_section}")

comm.Reduce(sum_for_section, mpi_sum, MPI.SUM, 0)
if my_rank == 0:
    print(f"total sum is {mpi_sum}")
