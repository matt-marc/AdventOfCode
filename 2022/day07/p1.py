#!/usr/bin/env python3

#
# Mathieu Marchildon
#

import numpy as np
import matplotlib.pyplot as plt
from anytree import Node, AnyNode, RenderTree, AsciiStyle, PostOrderIter, find

filename = f"../inputs/day07-input.txt"

file = open(filename, "r")
lines = file.readlines()
lines[:] = [line.strip().split() for line in lines[1:]]


def is_node(line):
    first_c = line[0]
    if first_c == "$":
        return False
    else:
        return True


def parse_node(line):
    first_c = line[0]
    if first_c == "dir":
        # print(f"dir with name = {line[1]}")
        return [line[1], "dir", 0]
    else:
        size = line[0]
        f = line[1]
        # print(f"file {f} with size {size}")
        return [f, "file", int(size)]


root = AnyNode(id="root", f_type="dir", size=0)
c_node = root


def print_tree():
    print(RenderTree(root, style=AsciiStyle()).by_attr("id"))

def print_tree2():
    for pre, fill , node in RenderTree(root):
        treestr = u"%s%s size =%s" % (pre, node.id, node.size)
        print(treestr)


for l in lines:
    if is_node(l):
        val = parse_node(l)
        new_node = AnyNode(id=val[0], f_type=val[1], size=val[2], parent=c_node)
    else:
        cmd = l[1]
        if cmd == "cd":
            new_dir = l[2]
            if new_dir == "..":
                c_node = c_node.parent
            elif new_dir == "/":
                c_node = root
                pass
            else:
                c_node = find(
                    c_node,
                    lambda node: node.id == new_dir and node.depth == c_node.depth + 1,
                )

            # input()
        elif cmd == "ls":
            pass


for node in PostOrderIter(root):
    if not node.parent == None:
        parent_dir = node.parent
        parent_dir.size = node.size + parent_dir.size

used_space = root.size
current_space = 70000000 - used_space
space_to_free = 30000000 - current_space
smallest = 70000000

for node in PostOrderIter(root):
    nsize = node.size
    if smallest > nsize and space_to_free < nsize:
        smallest = nsize


print(f"{used_space=}")
print(f"{current_space=}")
print(f"{space_to_free=}")
print(f"{smallest=}")
print(RenderTree(root))
print_tree()
print_tree2()
# print(total)
