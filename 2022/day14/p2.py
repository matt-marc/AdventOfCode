#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

filename = f"../inputs/day14-test-input.txt"
filename = f"../inputs/day14-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip() for line in lines]


# rmap = np.array([[]])5
w, h = 800, 200
start_sand = [500, 0]
max_y = 0
rmap = [["." for x in range(w)] for y in range(h)]


def coords_to_path(coords):
    start = coords[0]
    path = []
    # path.append(start)

    for i in range(1, len(coords)):
        pre_c = coords[i - 1]
        new_c = coords[i]

        if pre_c[0] == new_c[0]:  # travelling in y dir
            d_y = new_c[1] - pre_c[1]
            fix_x = pre_c[0]
            start_y = pre_c[1]
            for y in range(0, d_y, np.sign(d_y)):
                path.append([fix_x, start_y + y])

        else:  # travellin in x dir
            d_x = new_c[0] - pre_c[0]
            fix_y = pre_c[1]
            start_x = pre_c[0]
            for x in range(0, d_x, np.sign(d_x)):
                path.append([start_x + x, fix_y])

        path.append(new_c)

    return path


def get_path_coords(path):
    coords = []
    sections = path.split("->")
    for p in sections:
        cc = p.split(",")
        x = int(cc[0])
        y = int(cc[1])
        coords.append([x, y])

    return coords_to_path(coords)


def pp_map():
    p = PrettyTable()
    for row in rmap:
        p.add_row(row)
    print(p.get_string(header=False, border=False))


def sim_sand(pos):
    s_x = pos[0]
    s_y = pos[1]
    valid = True

    if s_y >= len(rmap) - 1:
        print("reached max depth")
        valid = False
        return [s_x, s_y], valid

    if rmap[s_y + 1][s_x] == ".":
        return [s_x, s_y + 1], valid

    if rmap[s_y + 1][s_x - 1] == ".":
        return [s_x - 1, s_y + 1], valid

    if rmap[s_y + 1][s_x + 1] == ".":
        return [s_x + 1, s_y + 1], valid

    if pos == start_sand:
        valid = False
        return pos, valid

    return pos, valid


print("generating map...")
for l in lines:
    path = get_path_coords(l)
    for p in path:
        px = p[0]
        py = p[1]
        if py > max_y:
            max_y = py
        rmap[py][px] = "#"

print("done")
print(f"max floor is {max_y}")

new_floor = max_y + 2
floor = f"0,{new_floor} -> {w-1},{new_floor}"

path = get_path_coords(floor)
for p in path:
    px = p[0]
    py = p[1]
    rmap[py][px] = "#"


sand_num = 0
is_valid = True

print("simulating sand...")
while is_valid:
    pre_sim = start_sand
    sim, is_valid = sim_sand(pre_sim)

    while not sim == pre_sim:
        pre_sim = sim
        sim, is_valid = sim_sand(pre_sim)


    #print(f"stand resting at {sim}")
    rmap[sim[1]][sim[0]] = "0"
    sand_num += 1

print("done")
print(f"total number of simulation {sand_num}")
