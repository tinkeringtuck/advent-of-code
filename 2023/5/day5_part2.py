from rich.pretty import pprint

with open("input.txt", "r") as input_stream:
    data = input_stream.read()

data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

almanac = {
    "seeds": [],
    "seed-to-soil": {},
    "soil-to-fertilizer": {},
    "fertilizer-to-water": {},
    "water-to-light": {},
    "light-to-temperature": {},
    "temperature-to-humidity": {},
    "humidity-to-location": {}
}

map_type = ""
for k, each in enumerate(data.split("\n")):
    if each.find("seeds") != -1:
        seeds = [int(x) for x in each.split(":")[1].split(" ") if x.isdigit()]  # seeds are now range not individual seed
        almanac["seeds"].extend(seeds)
        important_numbers = set(seeds)
        print(f"seeds are {almanac.get('seeds')}")
    elif each.find("map") != -1:
        temp = set()
        map_type = each.split(" ")[0]
        from_type = map_type.split("-")[0]
        to_type = map_type.split("-")[-1]
        print(f"{map_type} found")
    elif not each and map_type:
        important_numbers = temp
        print(f"{map_type} ended")
    elif not each and not map_type:
        pass # do nothing
    else:
        numbers = [int(x) for x in each.split(" ") if x.isdigit()]
        print(f"numbers for {map_type} are {numbers}")
        destination = numbers[0]
        source = numbers[1]
        num_range = numbers[2]
        for important in important_numbers:
            if important >= source and important <= source + num_range: # number is in range
                difference = important - source
                keep_destination = destination + difference
                print(f"source {important} and destination {keep_destination} for {map_type}")
                almanac[map_type].update({important: keep_destination})
                temp.add(keep_destination) # found in range
            else:
                temp.add(important) # must be same number  

pprint(almanac, expand_all=True)

locations = {}
# find location
for each in seeds:
    soil = almanac.get("seed-to-soil").get(each, each)
    fertilizer = almanac.get("soil-to-fertilizer").get(soil, soil)
    water = almanac.get("fertilizer-to-water").get(fertilizer, fertilizer)
    light = almanac.get("water-to-light").get(water, water)
    temperature = almanac.get("light-to-temperature").get(light, light)
    humidity = almanac.get("temperature-to-humidity").get(temperature, temperature)
    location = almanac.get("humidity-to-location").get(humidity, humidity)
    locations[each] = location

print(locations)

for k, v in enumerate(locations.values()):
    if k == 0:
        lowest = v
    elif v < lowest:
        lowest = v

print(f"the lowest location is {lowest}")


