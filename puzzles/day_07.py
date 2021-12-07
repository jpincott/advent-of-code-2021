def get_input():
    with open('../input/day_07.txt') as f:
        return list(map(int, f.read().split(",")))


def find_min_by(nums, fn=lambda x: x):
    return min(sum(fn(abs(n - i)) for n in nums) for i in range(min(nums), max(nums) + 1))


def main():
    nums = get_input()
    print(pt1 := find_min_by(nums))
    print(pt2 := find_min_by(nums, lambda x: x * (x + 1) // 2))


if __name__ == '__main__':
    main()
