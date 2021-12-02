from utils.io import stream_input


def get_input():
    return [(d[0], int(x)) for d, x in map(str.split, stream_input(day=2))]


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
                xpos += x
                depth += aim * x
            case 'd':
                aim += x
            case 'u':
                aim -= x
    print(pt2 := xpos * depth)


if __name__ == '__main__':
    main()
