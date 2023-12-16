import re
from rich import print

with open("input.txt", "r") as input_stream:
    data = input_stream.read()

# data = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""

dir_map = {"R": 1,
           "L": 0}

data_dict = {}
key_list = []

for k, each in enumerate(data.split("\n")):
    if k == 0:
        directions = each
    elif each:
        key = each.split(" ")[0]
        key_list.append(key)
        data_tuple = re.search('\((.*)\)', each).group(1)
        data_dict[key] = (data_tuple.split(", ")[0], data_tuple.split(", ")[1])

next_position = 'AAA'
moves = 0
while True:
    for each in directions:
        next_position = data_dict[next_position][dir_map[each]]
        moves += 1
        if next_position == 'ZZZ':
            break
    if next_position == 'ZZZ':
        break


print(f"the puzzle required {moves} moves")
