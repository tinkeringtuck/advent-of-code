import re

with open('input.txt', 'r') as input_stream:
    data = input_stream.read()

drop_alpha = re.sub("[^0-9\n]", "", data).split('\n')

print(sum([int(f"{each[0]}{each[-1]}") for each in drop_alpha]))