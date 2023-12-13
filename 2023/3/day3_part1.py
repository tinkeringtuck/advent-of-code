with open("input.txt", "r") as input_stream:
    data = input_stream.read()

data = """.......5......
..7*..*.....4*
...*13*......9
.......15.....
..............
..............
..............
..............
..............
..............
21............
...*9........."""

# need to add check for case like ...*13*...

print(f"{data}\n")
data = data.split("\n")
numbers = []

def find_adjacent(row, symbol_index):
    # knowing symbol index, look for adjacency
    # row may be prev, current, or next
    for char_index, char in enumerate(row):
        if not char.isdigit() and char != ".":
            temp = list(row)
            temp[char_index] = "."
            row = ''.join(temp)
    adjacent_parts = []
    row_parts = [x for x in row.split(".") if x and x.isdigit()]
    for part in row_parts:
        part_start = row.find(part)
        part_end = row.find(part) + len(part) - 1
        if part_start != -1:
            if abs(symbol_index - part_start) <= 1 or abs(symbol_index - part_end) <= 1:
                print(f"adjacent part {part} found")
                adjacent_parts.append(int(part))
    return adjacent_parts

def find_symbols(row):
    # find symbol(s) and return index(s)
    symbols = []
    for i, char in enumerate(row):
        if not char.isdigit() and char != '.':
            # print(f"symbol {char} found for {row} at index {i}")
            symbols.append(i)
    return symbols

for i, current_row in enumerate(data):
    current_symbols = find_symbols(current_row)
    if i == 0:
        # check current and next
        next_row = data[i+1]
        for symbol_index in current_symbols:
            print(f"current row: \t{current_row}")
            print(f"next row: \t{next_row}")
            print(f"checking current row for symbol at index {symbol_index}")
            numbers.extend(find_adjacent(current_row, symbol_index))
            print(f"checking next row for symbol at index {symbol_index}")
            numbers.extend(find_adjacent(next_row, symbol_index))
    elif i < len(data) - 1:
        # check current, next, and previous
        next_row = data[i+1]
        prev_row = data[i-1]
        for symbol_index in current_symbols:
            print(f"prev row: \t{prev_row}")
            print(f"current row: \t{current_row}")
            print(f"next row: \t{next_row}")
            print(f"checking prev row for symbol at index {symbol_index}")
            numbers.extend(find_adjacent(prev_row, symbol_index))
            print(f"checking current row for symbol at index {symbol_index}")
            numbers.extend(find_adjacent(current_row, symbol_index))
            print(f"checking next row for symbol at index {symbol_index}")
            numbers.extend(find_adjacent(next_row, symbol_index))
    else:
        # check current and previous
        prev_row = data[i-1]
        for symbol_index in current_symbols:
            print(f"prev row: \t{prev_row}")
            print(f"current row: \t{current_row}")
            print(f"checking prev row for symbol at index {symbol_index}")
            numbers.extend(find_adjacent(prev_row, symbol_index))
            print(f"checking current row for symbol at index {symbol_index}")
            numbers.extend(find_adjacent(current_row, symbol_index))

# print(f"part numbers found: {numbers}")
print(f"sum of numbers is {sum(numbers)}")