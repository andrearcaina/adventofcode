seeds = []
mappings = {}

with open('day5.txt', 'r') as f:
    curr = False
    
    for line in f:
        line = line.strip()
        if line:
            if not seeds: # gets first line
                seeds = line.split(': ')[1].split()
                seeds = [int(val) for val in seeds]
            if line.endswith(':'): # gets key
                curr = line[:-1]
                mappings[curr] = []
            elif curr: # gets values
                values = [int(val) for val in line.split()]
                mappings[curr].append(values)

    for ranges in mappings.values():
        new = []
        for seed in seeds:
            for offset, start, length in ranges:
                if start <= seed < start + length:
                    new.append(seed - start + offset)
                    break
            else:
                new.append(seed)
        seeds = new

print(min(seeds))
