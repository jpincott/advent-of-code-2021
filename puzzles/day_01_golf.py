with open('../input/day_01.txt') as f:
    d = list(map(int, f))
for n in (1, 3):
    print(sum(a < b for a, b in zip(d, d[n:])))
