with open("input.txt", "r") as input_stream:
    data = input_stream.read()

# data = """Time:      7  15   30
# Distance:  9  40  200"""


times = []
distances = []
for k, each in enumerate(data.split("\n")):
    if k % 2 == 0:
        times.extend([int(each.split(":")[1].replace(" ", ""))])
    else:
        distances.extend([int(each.split(":")[1].replace(" ", ""))])

winners = []
for time, distance in zip(times, distances):
    ranges = range(1, time)
    for each in ranges:
        time_left = time - each
        traveled = time_left * each
        if traveled > distance:
            least = each
            most = time - each
            num_winners = time - each - each + 1
            print(f"{num_winners} winning numbers")
            winners.append(num_winners)
            break
result = 1
for each in winners:
    result = result * each

print(f"result is {result}")