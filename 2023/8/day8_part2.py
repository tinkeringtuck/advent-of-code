import re
from rich import print
from math import lcm
from functools import reduce

with open("input.txt", "r") as input_stream:
    data = input_stream.read()

# data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

dir_map = {"R": 1,
           "L": 0}

data_dict = {}
key_list = []
starting_moves = []
for k, each in enumerate(data.split("\n")):
    if k == 0:
        directions = each
    elif each:
        key = each.split(" ")[0]
        key_list.append(key)
        data_tuple = re.search('\((.*)\)', each).group(1)
        data_dict[key] = (data_tuple.split(", ")[0], data_tuple.split(", ")[1])
        if key.endswith('A'):
            starting_moves.append(key)

number_of_starts = len(starting_moves)
print(f"starting moves are {starting_moves}")
moves_to_complete = []
for each in starting_moves:
    moves = 0
    next_position = each
    while True:
        stop = False
        for dir in directions:
            next_position = data_dict[next_position][dir_map[dir]]
            moves += 1
            if next_position.endswith("Z"):
                stop = True
                moves_to_complete.append(moves)
                print(f"ending {each} puzzle after {moves} moves")
                break
        if stop:
            break

print(f"end of puzzle solving, results: {moves_to_complete}")

least_common_multiple = reduce(lcm, moves_to_complete)

print(f"the least common multiple of all maps is {least_common_multiple}")