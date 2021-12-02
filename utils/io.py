def stream_lines(day):
    with open(f"../input/day_{day:02d}.txt") as f:
        yield from f
