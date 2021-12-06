from collections import Counter
from re import findall

from utils.io import stream_input


def get_input():
    return [
        ((x1, y1), (x2, y2))
        for x1, y1, x2, y2 in
        (map(int, findall("(\\d+)", l)) for l in stream_input(day=5))
    ]


def is_hv(pq):
    return any(pi == qi for pi, qi in zip(*pq))


def signum(n: int):
    return (n > 0) - (n < 0)


def cells_between(p, q):
    ds = (q[0] - p[0], q[1] - p[1])
    dx, dy = map(signum, ds)
    m = max(map(abs, ds))
    for n in range(m + 1):
        yield p[0] + n * dx, p[1] + n * dy


def main():
    pqs = get_input()
    print(pt1 := count_intersections(pq for pq in pqs if is_hv(pq)))
    print(pt2 := count_intersections(pqs))


def count_intersections(pqs, n=1):
    return sum(v > n for v in Counter(c for p, q in pqs for c in cells_between(p, q)).values())


if __name__ == '__main__':
    main()
