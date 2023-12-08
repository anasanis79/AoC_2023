class MyMap:
    def __init__(self, lines, start, end):
        self.sources_2_destinations = []
        for line in lines[start:end]:
            nums = [int(st) for st in line.split()]
            self.sources_2_destinations.append((nums[1], nums[1] + nums[2] - 1, nums[0]))
        self.sources_2_destinations.sort(key=lambda lst: lst[0])

    def get_destination(self, source):
        return next((s2d[2] + source - s2d[0] for s2d in self.sources_2_destinations if s2d[0] <= source <= s2d[1]), source)

    def get_destinations(self, source_start, source_end):
        result = []
        for s2d in self.sources_2_destinations:
            if s2d[0] <= source_start <= s2d[1]:
                result.append((s2d[2] + source_start - s2d[0], min(s2d[2] + source_end - s2d[0], s2d[1])))
                if source_end > s2d[1]:
                    source_start = s2d[1] + 1
                else:
                    return result
        result.append((source_start, source_end))
        return result

    def print_me(self):
        for s2d in self.sources_2_destinations:
            print(s2d)


def build_map(lines, start_line):
    i = 0
    while i < len(lines) and lines[i].find(start_line) < 0:
        i += 1
    i += 1
    start = i
    while i < len(lines) and len(lines[i]) > 1:
        i += 1
    end = i
    return MyMap(lines, start, end)


def calculate_from_file(f_name):
    with open(f_name) as f:
        lines = f.readlines()

    seeds = [int(st) for st in lines[0][lines[0].find(":") + 2:].split(" ")]
    # print(seeds)

    mm_seed_2_soil = build_map(lines, "seed-to-soil map:")
    mm_soil_2_fert = build_map(lines, "soil-to-fertilizer map:")
    mm_fert_2_water = build_map(lines, "fertilizer-to-water map:")
    mm_water_2_light = build_map(lines, "water-to-light map:")
    mm_light_2_temp = build_map(lines, "light-to-temperature map:")
    mm_temp_2_hum = build_map(lines, "temperature-to-humidity map:")
    mm_hum_2_location = build_map(lines, "humidity-to-location map:")

    min_destination = 99999999999
    for seed in seeds:
        d = mm_hum_2_location.get_destination(mm_temp_2_hum.get_destination(mm_light_2_temp.get_destination(mm_water_2_light.get_destination(mm_fert_2_water.get_destination(mm_soil_2_fert.get_destination(mm_seed_2_soil.get_destination(seed)))))))
        if d < min_destination:
            min_destination = d
    print("Part one: " + str(min_destination))

    min_destination = min(location[0]
                          for i in range(0, int(len(seeds) / 2))
                          for soil in mm_seed_2_soil.get_destinations(seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1] - 1)
                          for fert in mm_soil_2_fert.get_destinations(soil[0], soil[1])
                          for water in mm_fert_2_water.get_destinations(fert[0], fert[1])
                          for light in mm_water_2_light.get_destinations(water[0], water[1])
                          for temp in mm_light_2_temp.get_destinations(light[0], light[1])
                          for hum in mm_temp_2_hum.get_destinations(temp[0], temp[1])
                          for location in mm_hum_2_location.get_destinations(hum[0], hum[1]))

    print("Part two: " + str(min_destination))


calculate_from_file("input/day5.txt")
