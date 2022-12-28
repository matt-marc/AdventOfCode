#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
import parse as ps

filename = f"../inputs/day16-input.txt"
filename = f"../inputs/day16-test-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip() for line in lines]


graph = {}
flow_rate = {}
opened = {}
valve_list = []


x_f = "rate={};"

for l in lines:
    l_list = l.replace(",", "").split(" ")

    node = l_list[1]
    flowrate_s = l_list[4]
    flowrate = ps.parse(x_f, flowrate_s).fixed[0]
    valves = l_list[9:]

    # print(f"node {node} has flow rate {flowrate} and is connected to {valves}")

    valve_list.append(node)
    graph[node] = valves
    flow_rate[node] = int(flowrate)
    opened[node] = False


def find_all_steps(c_key, opened_valves, time):

    p_valves = []
    for v in valve_list:
        if not opened_valves[v]:
            p_valves.append(v)

    # while we have unchecked valves:
    level = 1

    # starts the valve queue at the given index with parent valve set to self
    valves_q = [[c_key, c_key, level, 0]]
    valves_l = valves_q

    print(f"total of {p_valves} need to be visited")
    print(f"\n\n\n")

    while p_valves:
        print(f"at level {level} we have to visit {p_valves} valves")
        print(f"valves to visit at level are {valves_l}")

        next_valves = []
        for v in valves_l:
            parent = v[0]
            children = graph[parent]
            c_level = v[2] + 1
            # print(f"iter in current level {v=}")
            # print(f"iter in current0 level {parent=} {children=}")
            print(children)

            for c in children:
                if c in p_valves:
                    weight = flow_rate[c] * (time - c_level - 1)
                    valves_q.append([c, parent, c_level, weight])
                    next_valves.append([c, parent, c_level, weight])
                    p_valves.remove(c)

        # print(f"{valves_q=}")
        valves_q.sort(key=lambda v: v[3], reverse=True)
        return valves_q


time = 30
start_v = "AA"
total_w = 0
option_stack = [[start_v, None, opened, time, total_w]]

for bfs_option in option_stack:
    starting_valve = bfs_option[0]
    parent_option = bfs_option[1]
    c_opened = bfs_option[2]
    c_time = bfs_option[3]
    c_w = bfs_option[4]
    print(f"starting at option {starting_valve}")
    input()

    if c_time > 0:
        all_options = find_all_steps(starting_valve, c_opened, c_time)

        for op in all_options:
            w = op[3]
            if w > 0:
                v = op[0]
                time_step = op[2]

                new_opened_valves = c_opened
                new_opened_valves[v] = True
                new_time = c_time - time_step
                new_w = c_w + w

                new_option = [
                    v,
                    bfs_option,
                    new_opened_valves,
                    new_time,
                    new_w
                ]
                option_stack.append(new_option)

            print(f"current options are")
            print(option_stack)
            input()

# while time > 0:
#    all_options = find_all_steps(start_v, c_opened, time)
#    # pick best answer
#    for op in all_options:
#        w = op[3]
#        if w > 0:
#            v = op[0]
#            time_step = op[2]
#            option_stack.append()
#
#    time = time - time_step
#    total_w += w_step
#    c_opened[v] = True
#    start_v = v
#
#    print(f"at time {time} and the best option is {valve_turn_off}")
#    input()
