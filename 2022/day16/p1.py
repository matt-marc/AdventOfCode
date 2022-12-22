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
weights = {}


x_f = "rate={};"

for l in lines:
    l_list = l.replace(",", "").split(" ")

    node = l_list[1]
    flowrate_s = l_list[4]
    flowrate = ps.parse(x_f, flowrate_s).fixed[0]
    valves = l_list[9:]

    print(f"node {node} has flow rate {flowrate} and is connected to {valves}")

    graph[node] = valves
    weights[node] = flowrate


def find_p(start_key):
    mins = 30
    c_key = start_key

    while mins > 0:
        # walk to valve
        mins = mins - 1
        c_flow = weights[c_key]
        c_valves = graph[c_key]


        max_p = weights[c_valves[0]]
        #find max pressure path
        for v in c_valves:
            max_p = max(max_p,weights[v])

        print(f"at valve {c_key} possible paths are {c_valves} with max flow at {max_p}")
        input()



find_p("DD")
