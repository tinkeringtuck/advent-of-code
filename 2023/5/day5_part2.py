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

seeds_range = [int(x) for x in data.split("\n")[0].split(":")[1].split(" ") if x.isdigit()]
seed_list = []
range_list = []

for k, each in enumerate(seeds_range):
    if k % 2 == 0:
        seed_list.append(each)
    else:
        range_list.append(each)

all_seeds = set()
for seed_start, seed_range in zip(seed_list, range_list):
    all_seeds.add(range(seed_start, seed_start+seed_range))


for k, each in enumerate(data.split("\n")):
    if each.find("seeds") != -1:
        # seeds = [int(x) for x in each.split(":")[1].split(" ") if x.isdigit()]  # seeds are now range not individual seed
        almanac["seeds"].extend(all_seeds)
        important_numbers = all_seeds  # using list of range, not list of seeds
        print(f"seeds are {almanac.get('seeds')}")
        pass
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
        source_range = range(source, source+num_range)
        destination_range = range(destination, destination+num_range)
        for important in important_numbers:
            overlap = range(max(source_range.start, important.start), min(source_range.stop, important.stop))
            if len(overlap) != 0:
                print(f"overlapping range {overlap} found")
                start_cutoff = overlap.start - source_range.start
                end_cutoff = source_range.stop - overlap.stop # minus 2 because stop is exclusive
                destination_keep = range(destination+start_cutoff, destination+num_range-end_cutoff)
                almanac[map_type].update({overlap: destination_keep})
            else:
                temp.add(important) # must be same number   

pprint(almanac, expand_all=True)

locations = {}
# find location
for each in all_seeds:
    temp_map = almanac.get("seed-to-soil")
    if not temp_map:
        temp_map = dict(zip(each, each))
    soil = set()
    for temp_key in temp_map:
        overlap = range(max(temp_key.start, each.start), min(temp_key.stop, each.stop))
        if len(overlap) != 0:
            start_cutoff = overlap.start - temp_key.start
            end_cutoff = temp_key.stop - overlap.stop
            soil.add(range(temp_map[temp_key].start+start_cutoff, temp_map[temp_key].stop-end_cutoff))
        else:
            soil.add(each)
    temp_map = almanac.get("soil-to-fertilizer")
    if not temp_map:
        temp_map = dict(zip(soil, soil))
    fertilizer = set()
    for temp_key in temp_map:
        for source in soil:
            overlap = range(max(temp_key.start, source.start), min(temp_key.stop, source.stop))
            if len(overlap) != 0:
                start_cutoff = overlap.start - temp_key.start
                end_cutoff = temp_key.stop - overlap.stop
                fertilizer.add(range(temp_map[temp_key].start+start_cutoff, temp_map[temp_key].stop-end_cutoff))
            else:
                fertilizer.add(source)
    temp_map = almanac.get("fertilizer-to-water")
    if not temp_map:
        temp_map = dict(zip(fertilizer, fertilizer))
    water = set()
    for temp_key in temp_map:
        for source in fertilizer:
            overlap = range(max(temp_key.start, source.start), min(temp_key.stop, source.stop))
            if len(overlap) != 0:
                start_cutoff = overlap.start - temp_key.start
                end_cutoff = temp_key.stop - overlap.stop
                water.add(range(temp_map[temp_key].start+start_cutoff, temp_map[temp_key].stop-end_cutoff))
            else:
                water.add(source)
    temp_map = almanac.get("water-to-light")
    if not temp_map:
        temp_map = dict(zip(water, water))
    light = set()
    for temp_key in temp_map:
        for source in water:
            overlap = range(max(temp_key.start, source.start), min(temp_key.stop, source.stop))
            if len(overlap) != 0:
                start_cutoff = overlap.start - temp_key.start
                end_cutoff = temp_key.stop - overlap.stop
                light.add(range(temp_map[temp_key].start+start_cutoff, temp_map[temp_key].stop-end_cutoff))
            else:
                light.add(source)
    temp_map = almanac.get("light-to-temperature")
    if not temp_map:
        temp_map = dict(zip(light, light))
    temperature = set()
    for temp_key in temp_map:
        for source in light:
            overlap = range(max(temp_key.start, source.start), min(temp_key.stop, source.stop))
            if len(overlap) != 0:
                start_cutoff = overlap.start - temp_key.start
                end_cutoff = temp_key.stop - overlap.stop
                temperature.add(range(temp_map[temp_key].start+start_cutoff, temp_map[temp_key].stop-end_cutoff))
            else:
                temperature.add(source)
    temp_map = almanac.get("temperature-to-humidity")
    if not temp_map:
        temp_map = dict(zip(temperature, temperature))
    humidity = set()
    for temp_key in temp_map:
        for source in temperature:
            overlap = range(max(temp_key.start, source.start), min(temp_key.stop, source.stop))
            if len(overlap) != 0:
                start_cutoff = overlap.start - temp_key.start
                end_cutoff = temp_key.stop - overlap.stop
                humidity.add(range(temp_map[temp_key].start+start_cutoff, temp_map[temp_key].stop-end_cutoff))
            else:
                humidity.add(source)
    temp_map = almanac.get("humidity-to-location")
    if not temp_map:
        temp_map = dict(zip(humidity, humidity))
    location = set()
    for temp_key in temp_map:
        for source in humidity:
            overlap = range(max(temp_key.start, source.start), min(temp_key.stop, source.stop))
            if len(overlap) != 0:
                start_cutoff = overlap.start - temp_key.start
                end_cutoff = temp_key.stop - overlap.stop
                location.add(range(temp_map[temp_key].start+start_cutoff, temp_map[temp_key].stop-end_cutoff))
            else:
                location.add(source)
    locations[each] = location

pprint(locations, expand_all=True)
# for k, v in enumerate(locations.values()):
#     if k == 0:
#         lowest = v
#     elif v < lowest:
#         lowest = v

# print(f"the lowest location is {lowest}")


