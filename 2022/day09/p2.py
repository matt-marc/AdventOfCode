#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import turtle
from turtle import *

filename = f"../inputs/day09-input.txt"
#filename = f"../inputs/day09-test-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip().split() for line in lines]


x = 0
y = 0
head = [[x, y]]

for line in lines:
    direction = line[0]
    spaces = int(line[1])

    for delta in range(spaces):
        if direction == "U":
            y += 1
        elif direction == "D":
            y -= 1
        elif direction == "R":
            x += 1
        elif direction == "L":
            x -= 1

        head.append([x, y])


def tail_pos(p1, p2, tail_p):
    px1 = p1[0]
    py1 = p1[1]
    px2 = p2[0]
    py2 = p2[1]

    m_delta_x = abs(px2 - px1)
    m_delta_y = abs(py2 - py1)

    h_delta_x1 = abs(px1 - tail_p[0])
    h_delta_y1 = abs(py1 - tail_p[1])
    h_delta_x2 = abs(px2 - tail_p[0])
    h_delta_y2 = abs(py2 - tail_p[1])

    #print(f"head moved from {p1} -> {p2}")
    if m_delta_x == 1 and m_delta_y == 1:
        if h_delta_x2 > 1 or h_delta_y2 > 1:
            #print("diagonal move")
            x_move = px2 - px1
            y_move = py2 - py1

            new_t = []
            if h_delta_x2 == 0:
                new_t = [tail_p[0], tail_p[1] + y_move]
            elif h_delta_y2 == 0:
                new_t = [tail_p[0] + x_move, tail_p[1]]
            else:
                new_t = [tail_p[0] + x_move, tail_p[1] + y_move]
            #print(f"{tail_p=}")
            #print(f"{new_t=}")
            return new_t
        else:
            #print(f"{tail_p=}")
            return tail_p


    if h_delta_x2 > 1:
        #print(f"head moved away from tail x dir")
        return [px1, py1]
    elif h_delta_y2 > 1:
        #print(f"head moved away from tail y dir")
        return [px1, py1]
    else:
        #print(f"no move")
        return tail_p


tail = [[0, 0]]
snake = [head]
for t in range(9):
    # start new tail at same position of the head
    tail = [head[0]]

    for i in range(len(head) - 1):
        #print(f"{tail[i]=}")
        new_tail = tail_pos(head[i], head[i + 1], tail[i])
        #print(f"{new_tail=}")
        tail.append(new_tail)

    snake.append(tail)
    head = tail



nparr = np.array(snake[9])
unique_tail = np.unique(nparr, axis=0)
plt.show()
print(len(unique_tail))
