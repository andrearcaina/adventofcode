SUM = 0
coords = set()

with open('day3.txt', 'r') as f:
    lines = []
    for line in f:
        chars = []
        for char in line.strip():
            chars.append(char)
        lines.append(chars)

    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            if ch not in '0123456789.':
                for x in range(r - 1, r + 2):
                    for y in range(c - 1, c + 2):
                        if 0 <= x < len(lines) and 0 <= y < len(lines[x]) and lines[x][y].isdigit():
                            while y > 0 and lines[x][y - 1].isdigit():
                                y -= 1
                            coords.add((x, y))

    adjacent_numbs = []
    coords = list(coords)

    for tup in coords:
        ch = ''
        row, col = tup[0], tup[1]

        while col < len(lines[row]) and lines[row][col].isdigit():
            ch += lines[row][col]
            col += 1
        adjacent_numbs.append(int(ch))

    SUM = sum(adjacent_numbs)

print(SUM)