with open("input.txt", "r") as input_stream:
    data = input_stream.read()

# data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

totals = []
for game in data.split("\n"):
    game_id = game.split(":", 1)[0].split(" ")[-1]
    minus_header = game.split(":")[1]
    print(f"starting game {game_id}")
    all_possible = True
    while True:
        for k, round in enumerate(minus_header.split(";")):
            print(f"starting round '{round}' for game {game_id}")
            for cubes in round.split(","):
                # is it red, blue, or green
                for each in limits:
                    if cubes.find(each) != -1:
                        num = cubes.split(" ")[1]
                        if int(num) <= int(limits[each]):
                            print(f"{num} {each} cubes is possible")
                        else:
                            print(f"{num} {each} cubes is not possible")
                            print("along for the ride :(")
                            all_possible = False
        if k == len(minus_header.split(";")) - 1:
            if all_possible:
                totals.append(int(game_id))
            break
    
print(sum(totals))