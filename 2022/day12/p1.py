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


#           y  x
# print(lines[0][0])
# lol
end_node = find_chr("E")
start_node = find_chr("S")
lines[start_node[0]][start_node[1]] = "a"
lines[end_node[0]][end_node[1]] = "z"

i = 0
node_stack = [start_node]
pre_node = [start_node]
print(f"start node is at {start_node=}")
print(f"final node is at {end_node=}")

while True:
    new_node = node_stack[i]
    bfs_nodes = get_next_nodes(new_node)

    if new_node == end_node:
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


print("DONE")

bk_node = node_stack[-1]
steps = 1
bfs_path = []
# print(f"starting bk trace from {bk_node}")
# print(f"{node_stack=}")
# print(f"{pre_node=}")

while not bk_node == start_node:
    bfs_path.insert(0, bk_node)
    node_idx = node_stack.index(bk_node)
    bk_node = pre_node[node_idx]

print(bfs_path)
print(len(bfs_path)-1)


#val_list = []
#for i in lines:
#    row_list = []
#    for c in i:
#        row_list.append(ord(c))
#
#    val_list.append(row_list)


#z = np.array(val_list)
#fig = plt.figure()
#X, Y = np.meshgrid(x_max, y_max)
#ax = plt.axes(projection="3d")
#w = ax.plot_surface(X, Y, z, cmap='coolwarm')
#plt.show()
#h =plt.hist2d(X, Y, z)
#plt.colorbar(h[3])
#input()
