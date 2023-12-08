import functools
import math

Times = [40, 82, 84, 92]
Distances = [233, 1011, 1110, 1487]

T = 40828492
D = 233101111101487


def delta(a, b, c):
    return b * b - 4 * a * c


def min_t_to_reach(t, d):
    return (t + math.sqrt(delta(1, -t, d))) / 2


def num_of_possible_ts(t, d):
    return 2 * int(min_t_to_reach(t, d)) - t + 1


possible_ways = [num_of_possible_ts(Times[i], Distances[i]) for i in range(len(Times))]

print("Part one: " + str(functools.reduce(lambda x, y: x*y, possible_ways)))

print("Part two: " + str(num_of_possible_ts(T, D)))

