def to_2d_rect(letter_str, width=None):
    lines = letter_str.strip("\n").split("\n")
    min_leading = min((len(line) - len(line.lstrip(' ')) for line in lines if line.strip()),default=0)
    lines = [line[min_leading:] for line in lines]
    lines = [line.rstrip() for line in lines]
    while len(lines) < 7:
        lines.insert(0, "")
    if width is None:
        width = max(len(line) for line in lines)
    return [list(line.ljust(width)) for line in lines]
