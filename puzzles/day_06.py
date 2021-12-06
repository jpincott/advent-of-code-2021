from collections import Counter


def get_input():
    with open('../input/day_06.txt') as f:
        return Counter(map(int, f.read().split(",")))


def main():
    c = get_input()
    print(sum(evolve(c, 80).values()))
    print(sum(evolve(c, 256).values()))


def evolve(c, n):
    for _ in range(n):
        v = c.get(0, 0)
        c = Counter({k - 1: v for k, v, in c.items() if k}) + Counter({6: v, 8: v})
    return c


if __name__ == '__main__':
    main()
