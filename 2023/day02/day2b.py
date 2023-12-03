SUM = 0

with open('day2.txt', 'r') as f:
    for i, line in enumerate(f):
        ID = i + 1
        line = line.strip().split(": ")[1].split("; ")
        
        MAX = {'red': 0, 'green': 0, 'blue': 0}

        for game in line:
            total = {'red': 0, 'green': 0, 'blue': 0}
            
            for set in game.split(", "):
                bag = [cube for cube in set.split()]
                total[bag[1]] = int(bag[0])

            for k, v in MAX.items():
                MAX[k] = max(v, total[k])
        
        else:
            SUM += MAX['red'] * MAX['green'] * MAX['blue']

print(SUM)