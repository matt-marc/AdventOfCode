#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import parse as ps
import progressbar

filename = f"../inputs/day15-test-input.txt"
filename = f"../inputs/day15-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip() for line in lines]


sb_list = []
beacs = []

x_min = 10
x_max = 10
y_scan = 2000000
# y_scan = 10

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


count = 0
print(f"min x is {x_min}")
print(f"max x is {x_max}")

for x in range(x_min - 40, x_max + 40):
    x_p = np.array([x, y_scan])
    # print(f"checking point {x_p}")

    for s in sb_list:
        sensor_pos = s[0]
        l1_sensor = s[2]
        l1_point = np.linalg.norm(x_p - sensor_pos, ord=1)
        # print(f"checking point with sensor {sensor_pos}")
        # print(f"l1 beacon {l1_sensor} l1 point{l1_point}")
        if l1_point <= l1_sensor:
            # if l1_point in beacon_pos:
            #    break
            # print(f"point {x_p} is within range of sensor {s}")
            count += 1
            break


print(count - 1)
