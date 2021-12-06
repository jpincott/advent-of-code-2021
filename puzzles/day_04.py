from itertools import chain

from more_itertools import collapse, first, last


def get_input():
    with open("../input/day_04.txt") as f:
        nums, *boards = f.read().split("\n\n")
        nums = [int(n) for n in nums.split(',')]
        boards = [Board([[int(n) for n in l.split()] for l in b.splitlines()]) for b in boards]
        return nums, boards


class Board:

    def __init__(self, grid: list[list[int]]):
        self.runs = list(map(set, chain(grid, zip(*grid))))
        self.nums = set(collapse(grid))

    def is_winner(self, called: set[int]):
        return any(s <= called for s in self.runs)

    def uncalled(self, called: set[int]):
        return self.nums - called


def play(nums, boards):
    for i, n in enumerate(nums):
        called = set(nums[:i+1])
        for b in boards:
            if b.is_winner(called):
                boards.remove(b)
                yield n * sum(b.uncalled(called))


def main():
    nums, boards = get_input()
    print(pt1 := first(play(nums, boards)))
    print(pt2 := last(play(nums, boards)))


if __name__ == '__main__':
    main()
