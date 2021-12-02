def get_input():
    with open('../input/day_02.txt') as f:
        return [(d[0], int(x)) for d, x in (l.split() for l in f)]


def main():
    steps = get_input()

    xpos = depth = 0
    for d, x in steps:
        match d:
            case 'f':
                xpos += x
            case 'd':
                depth += x
            case 'u':
                depth -= x
    print(pt1 := xpos * depth)

    xpos = depth = aim = 0
    for d, x in steps:
        match d:
            case 'f':
                xpos, depth = xpos + x, depth + aim * x
            case 'd':
                aim = aim + x
            case 'u':
                aim = aim - x
    print(pt2 := xpos * depth)


if __name__ == '__main__':
    main()
