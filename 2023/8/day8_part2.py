import re
from rich import print

with open("input.txt", "r") as input_stream:
    data = input_stream.read()

data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

dir_map = {"R": 1,
           "L": 0}

data_dict = {}
key_list = []
starting_moves = set()
for k, each in enumerate(data.split("\n")):
    if k == 0:
        directions = each
    elif each:
        key = each.split(" ")[0]
        key_list.append(key)
        data_tuple = re.search('\((.*)\)', each).group(1)
        data_dict[key] = (data_tuple.split(", ")[0], data_tuple.split(", ")[1])
        if key.endswith('A'):
            starting_moves.add(key)

moves = 0
number_of_starts = len(starting_moves)
next_moves = starting_moves
print(f"starting moves are {starting_moves}")
while True:
    stop = False
    for each in directions:
        temp_moves = set()
        for key in next_moves:        
            next_position = data_dict[key][dir_map[each]]
            temp_moves.add(next_position)
        moves += 1
        next_moves = temp_moves
        print(f"end of {moves} move, resulted in {next_moves}")
        if all(x.endswith("Z") for x in temp_moves):
            stop = True
            break
    if stop:
        break


print(f"the puzzle required {moves} moves")