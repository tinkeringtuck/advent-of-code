with open("input.txt", "r") as input_stream:
    data = input_stream.read()

data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

rank = {1: 1,
        2: 2,
        3: 4,
        4: 4,
        5: 5}

hands = {}

for each in data.split("\n"):
    hand = each.split(" ")[0]
    hands[hand] = {}
    bid = each.split(" ")[1]
    print(f"hand {hand} for {bid} bid")
    counts = {"A": {"count": 0, "strength": 12},
              "K": {"count": 0, "strength": 11},
              "Q": {"count": 0, "strength": 10},
              "J": {"count": 0, "strength": 0},
              "T": {"count": 0, "strength": 9},
              "9": {"count": 0, "strength": 8},
              "8": {"count": 0, "strength": 7},
              "7": {"count": 0, "strength": 6},
              "6": {"count": 0, "strength": 5},
              "5": {"count": 0, "strength": 4},
              "4": {"count": 0, "strength": 3},
              "3": {"count": 0, "strength": 2},
              "2": {"count": 0, "strength": 1}}
    for char in hand:
        counts[char]["count"] += 1
    result = {}
    for char in counts:
        if counts[char]["count"] > 1:
            result[char] = counts[char]["count"]
