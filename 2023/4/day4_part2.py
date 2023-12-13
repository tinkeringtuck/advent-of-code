with open("input.txt", "r") as input_stream:
    data = input_stream.read()

data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

total = []
card_dict = {}
new_card = []

def score_card(winners, drew):
    score = 0
    for winner in winners:
        for number in drew:
            if winner == number:
                score += 1
                print("score increases by 1")
    return score


for row in data.split("\n"):
    score = 0
    numbers = row.split(":")
    card = int(numbers[0].split(" ")[1])
    winners = [x for x in numbers[1].split("|")[0].split(" ") if x.isdigit()]
    mine = [x for x in numbers[1].split("|")[1].split(" ") if x.isdigit()]
    card_dict[card] = {"winners": winners, "mine": mine}

for k, card in enumerate(card_dict):
    max = len(card_dict) - 1
    score = score_card(card_dict[card]["winners"], card_dict[card]["mine"])
    if k + score < max: # 1 card for each score past k 
        for each in range(card+1, card+1+score):
            new_card.append(card_dict[each])
    else: # do not add past max
        for each in range(card, max+1):
            new_card.append(card_dict[each])

# for each in new_card:
#     total.append(score_card(each["winners"], each["mine"]))



print(f"total score is {len(new_card)}")