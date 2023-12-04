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
            if ch.isdigit() or ch == '.':
                continue
            else: 
                for x in range(r - 1, r + 2):
                    for y in range(c - 1, c + 2):
                        if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[x]) or not lines[x][y].isdigit():
                            continue
                        else:
                            while y > 0 and lines[x][y - 1].isdigit():
                                y -= 1
                            coords.add((x, y))

    adjacent_numbs = []
    
    coords = list(coords)

    for tup in coords:
        ch = ''
        x, y = tup[0], tup[1]

        while y < len(lines[r]) and lines[x][y].isdigit():
            ch += lines[x][y]
            y += 1
        adjacent_numbs.append(int(ch))

    SUM = sum(adjacent_numbs)

print(SUM)