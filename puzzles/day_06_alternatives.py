from collections import Counter

from utils.decorators import timed


def get_input():
    with open('../input/day_06.txt') as f:
        return Counter(map(int, f.read().split(",")))


def main():
    c = get_input()
    print(sum(use_counter(c, 80).values()))
    print(sum(use_counter(c, 256).values()))

    l = [c.get(i, 0) for i in range(9)]
    print(sum(use_list(l, 80)))
    print(sum(use_list(l, 256)))


@timed
def use_counter(c, n):
    for _ in range(n):
        c = Counter({k - 1: v for k, v, in c.items() if k}) + Counter({6: (v := c.get(0, 0)), 8: v})
    return c


@timed
def use_list(l, n):
    for _ in range(n):
        l = l[1:] + l[0:1]
        l[6] += l[8]
    return l


if __name__ == '__main__':
    main()
