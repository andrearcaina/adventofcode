steps = []
tree = {}
current = 'AAA'
count = 0

with open('day8.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not steps: # gets first line
            steps = list(line)
        elif line: # if line and steps exists
            node = line.split(sep=' = ') # get root node and children
            root, children = node[0], node[1][1:-1].split(', ')
            tree[root] = children # add to network (dict)

    while current != 'ZZZ':
        count += 1
        traverse = 0 if steps[0] == 'L' else 1
        current = tree[current][traverse]
        steps = steps[1:] + [steps[0]]

print(count)