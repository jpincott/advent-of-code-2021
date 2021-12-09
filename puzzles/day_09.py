from functools import reduce
from math import prod

from more_itertools import take

from utils.io import stream_input


def get_input():
    return {
        complex(x, y): int(n)
        for y, l in enumerate(stream_input(day=9))
        for x, n in enumerate(l.strip())
    }


def get_lows(nums):
    for x in range(100):
        for y in range(100):
            z = complex(x, y)
            v = nums[z]
            if all(v < nums.get(z + d, 9) for d in (1, -1, 1j, -1j)):
                yield z, v


def get_basin(nums, seeds, basin):
    if not seeds:
        return basin

    seeds = reduce(set.union, ({z for d in (1, -1, 1j, -1j) if nums.get(z := (s + d), 9) < 9} for s in seeds))
    return get_basin(nums, seeds - basin, basin | seeds)


def main():
    nums = get_input()

    lows = list(get_lows(nums))
    print(pt1 := sum(1 + v for _, v in lows))

    basins = (get_basin(nums, {z}, set()) for z, _ in lows)
    print(pt2 := prod(take(3, sorted(map(len, basins), reverse=True))))


if __name__ == '__main__':
    main()
