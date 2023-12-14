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
    "seed-to-soil": {"parent": "seeds"},
    "soil-to-fertilizer": {"parent": "seed-to-soil"},
    "fertilizer-to-water": {"parent": "fertilizer-to-water"},
    "water-to-light": {"parent": "fertilizer-to-water"},
    "light-to-temperature": {"parent": "water-to-light"},
    "temperature-to-humidity": {"parent": "light-to-temperature"},
    "humidity-to-location": {"parent": "temperature-to-humidity"}
}

map_type = ""
for k, each in enumerate(data.split("\n")):
    if each.find("seeds") != -1:
        seeds = [int(x) for x in each.split(":")[1].split(" ") if x.isdigit()]
        almanac["seeds"].extend(seeds)
        print(f"seeds are {almanac.get('seeds')}")
    elif each.find("map") != -1:
        map_type = each.split(" ")[0]
        from_type = map_type.split("-")[0]
        to_type = map_type.split("-")[-1]
        print(f"{map_type} found")
    elif not each and map_type:
        print(f"{map_type} ended")
    elif not each and not map_type:
        pass # do nothing
    else:
        numbers = [int(x) for x in each.split(" ") if x.isdigit()]
        print(f"numbers for {map_type} are {numbers}")
        destination = numbers[0]
        source = numbers[1]
        num_range = numbers[2]
        source_nums = [x for x in range(source, source+num_range)]
        destination_nums = [x for x in range(destination, destination+num_range)]
        temp_map = {k:v for (k,v) in zip(source_nums, destination_nums)}
        # temp_map = {range(source, source+num_range), range(destination, destination+num_range)}
        almanac[map_type].update(temp_map)
        print(f"added {numbers} for {map_type}")
        print(f"the {map_type} map is {temp_map}")

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


