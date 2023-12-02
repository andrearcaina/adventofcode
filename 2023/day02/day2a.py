SUM = 0

with open('day2.txt', 'r') as f:
    for i, line in enumerate(f):
        ID = i + 1
        line = line.strip().split(": ")[1].split("; ")

        for game in line:
            total = {'red': 0, 'green': 0, 'blue': 0}
            
            for set in game.split(", "):
                bag = [cube for cube in set.split()]
                total[bag[1]] = int(bag[0])

            if total["red"] > 12 or total["green"] > 13 or total["blue"] > 14:
                break

        else:
            SUM += ID

print(SUM)