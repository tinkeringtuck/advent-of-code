with open("input.txt", "r") as input_stream:
    data = input_stream.read()

# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

total = []
for row in data.split("\n"):
    score = 0
    numbers = row.split(":")
    card = numbers[0]
    winners = [x for x in numbers[1].split("|")[0].split(" ") if x.isdigit()]
    mine = [x for x in numbers[1].split("|")[1].split(" ") if x.isdigit()]
    
    for winner in winners:
        for number in mine:
            if winner == number:
                print(f"winning # {winner} found for {card}")
                if score == 0:
                    score += 1
                    print("score increases by 1")
                else:
                    score = score * 2
                    print("score doubles")
    total.append(score)
    print(f"winning #s for {card}\t{winners}")
    print(f"my #s for {card}\t{mine}")

print(f"total score is {sum(total)}")