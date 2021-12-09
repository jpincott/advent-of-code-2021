from collections import Counter
from itertools import chain
from operator import itemgetter

from more_itertools import one

from utils.io import stream_input


def get_input():
    return [[s.split() for s in line.split('|')] for line in stream_input(day=8)]


def decode(signals):
    c = Counter(chain.from_iterable(signals))
    d = {v: k for k, v in c.items()}
    d = {'B': d[6], 'E': d[4], 'F': d[9]}

    s = list(sorted(signals, key=len))
    d['C'] = one(x for x in s[0] if x not in d.values())
    d['A'] = one(x for x in s[1] if x not in d.values())
    d['D'] = one(x for x in s[2] if x not in d.values())
    d['G'] = one(x for x in s[9] if x not in d.values())

    return {v: k for k, v in d.items()}


def translate(signals, decoder):
    digits = {
        'ABCEFG': '0',
        'CF': '1',
        'ACDEG': '2',
        'ACDFG': '3',
        'BCDF': '4',
        'ABDFG': '5',
        'ABDEFG': '6',
        'ACF': '7',
        'ABCDEFG': '8',
        'ABCDFG': '9'
    }
    return int("".join(digits["".join(sorted(decoder[c] for c in s))] for s in signals))


def main():
    observations = get_input()
    print(pt1 := sum(len(s) in (2, 3, 4, 7) for s in chain.from_iterable(map(itemgetter(1), observations))))
    print(pt2 := sum(translate(outputs, decode(inputs)) for inputs, outputs in observations))


if __name__ == '__main__':
    main()
