from functools import reduce

from utils.io import stream_input


def get_input():
    return [(d[0], int(x)) for d, x in map(str.split, stream_input(day=2))]


def main():
    steps = get_input()

    directions = {'f': 1, 'd': 1j, 'u': -1j}
    sub = sum(directions[d] * x for d, x in steps)
    print(pt1 := f"{sub.real * sub.imag:.0f}")

    actions = {
        'f': lambda sub, aim, x: (sub + complex(x, aim * x), aim),
        'd': lambda sub, aim, x: (sub, aim + x),
        'u': lambda sub, aim, x: (sub, aim - x)
    }
    sub, _ = reduce(lambda state, step: actions[step[0]](*state, step[1]), steps, (0, 0))
    print(pt2 := f"{sub.real * sub.imag:.0f}")


if __name__ == '__main__':
    main()
