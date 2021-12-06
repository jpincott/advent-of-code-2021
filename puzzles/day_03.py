from functools import reduce

from utils.io import stream_input


def get_input():
    return [n.strip() for n in stream_input(day=3)]


def most_common_value(nums, bit):
    return int(2 * sum(int(n[bit]) for n in nums) >= len(nums))


def least_common_value(nums, bit):
    return 1 - most_common_value(nums, bit)


def find_one_by(fn, nums, bit=0):
    return int(nums[0], 2) if len(nums) == 1 \
        else find_one_by(fn, [n for n in nums if int(n[bit]) == fn(nums, bit)], bit + 1)


def main():
    nums = get_input()
    bits = len(nums[0])

    gamma = reduce(lambda acc, i: (acc << 1) | most_common_value(nums, i), range(bits), 0)
    epsilon = ~gamma % (1 << bits)
    print(pt1 := gamma * epsilon)

    ogr = find_one_by(most_common_value, nums)
    co2 = find_one_by(least_common_value, nums)
    print(pt2 := ogr * co2)


if __name__ == '__main__':
    main()
