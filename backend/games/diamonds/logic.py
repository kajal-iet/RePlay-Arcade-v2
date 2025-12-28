def outline(size):
    lines = []
    for i in range(size):
        lines.append(' ' * (size - i - 1) + '/' + ' ' * (i * 2) + '\\')
    for i in range(size):
        lines.append(' ' * i + '\\' + ' ' * ((size - i - 1) * 2) + '/')
    return lines

def filled(size):
    lines = []
    for i in range(size):
        lines.append(' ' * (size - i - 1) + '/' * (i + 1) + '\\' * (i + 1))
    for i in range(size):
        lines.append(' ' * i + '\\' * (size - i) + '/' * (size - i))
    return lines

def rotate(lines):
    max_len = max(len(line) for line in lines)
    padded = [line.ljust(max_len) for line in lines]
    return [''.join(row[::-1]) for row in zip(*padded)]
