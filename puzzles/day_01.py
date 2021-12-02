from itertools import pairwise

from more_itertools import windowed

from utils.io import stream_lines


def get_input():
    return [int(line) for line in stream_lines(1)]


def main():
    depths = get_input()

    # Using itertools and brute force
    print(sum(a < b for a, b in pairwise(depths)))
    print(sum(a < b for a, b in pairwise(map(sum, windowed(depths, 3)))))

    # Using builtins only and spotting the optimisation in part 2
    print(sum(a < b for a, b in zip(depths, depths[1:])))
    print(sum(a < b for a, b in zip(depths, depths[3:])))


if __name__ == '__main__':
    main()
