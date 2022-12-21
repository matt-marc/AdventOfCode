#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt

filename = f"../inputs/day12-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [list(line.strip()) for line in lines]

y_max = len(lines)
x_max = len(lines[0])


def find_chr(c):
    for i in lines:
        if c in i:
            y_val = lines.index(i)
            x_val = lines[y_val].index(c)
            return [y_val, x_val]

def find_all_chr(c):
    n_list = []
    for i in lines:
        if c in i:
            y_val = lines.index(i)
            x_val = lines[y_val].index(c)
            n_list.append([y_val, x_val])

    return n_list

def get_next_nodes(pos):
    p_x = pos[1]
    p_y = pos[0]
    val = ord(lines[p_y][p_x])

    # print(f"at point {pos} value of {chr(val)}")
    if p_y == 0:
        down = ord(lines[p_y + 1][p_x]) - val
        up = 2
    elif p_y == y_max - 1:
        down = 2
        up = ord(lines[p_y - 1][p_x]) - val
    else:
        down = ord(lines[p_y + 1][p_x]) - val
        up = ord(lines[p_y - 1][p_x]) - val

    if p_x == 0:
        left = 2
        right = ord(lines[p_y][p_x + 1]) - val
    elif p_x == x_max - 1:
        left = ord(lines[p_y][p_x - 1]) - val
        right = 2
    else:
        left = ord(lines[p_y][p_x - 1]) - val
        right = ord(lines[p_y][p_x + 1]) - val

    # print(f"{up=} {right=} {down=} {left=}")

    # get possible nodes
    walking_nodes = []
    if up < 2:
        walking_nodes.append([p_y - 1, p_x])
    if down < 2:
        walking_nodes.append([p_y + 1, p_x])
    if left < 2:
        walking_nodes.append([p_y, p_x - 1])
    if right < 2:
        walking_nodes.append([p_y, p_x + 1])

    # print(f"{walking_nodes=}")
    return walking_nodes


def find_minpath(s_node, e_node):
    i = 0
    node_stack = [s_node]
    pre_node = [s_node]

    while True:
        new_node = node_stack[i]
        bfs_nodes = get_next_nodes(new_node)

        if new_node == e_node:
            # found end
            break

        for node in bfs_nodes:
            if not node in node_stack:
                # print(f"{node=} has not been visited")
                node_stack.append(node)
                # Adds previous node to other stack
                pre_node.append(new_node)

        # print(f"{node_stack=}")
        i += 1

    bk_node = node_stack[-1]
    steps = 1
    bfs_path = []

    while not bk_node == s_node:
        bfs_path.insert(0, bk_node)
        node_idx = node_stack.index(bk_node)
        bk_node = pre_node[node_idx]

    return len(bfs_path) - 1


#           y  x
# print(lines[0][0])
# lol
end_node = find_chr("E")
start_node = find_chr("S")
lines[start_node[0]][start_node[1]] = "a"
lines[end_node[0]][end_node[1]] = "z"

print(f"start node is at {start_node=}")
print(f"final node is at {end_node=}")

all_a = find_all_chr('a')
min_path = find_minpath(start_node, end_node)

for n in all_a:
    new_min = find_minpath(n, end_node)
    if new_min < min_path:
        min_path = new_min

print(min_path)

