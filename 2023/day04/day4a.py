points = 0

with open('day4.txt', 'r') as f:
    for line in f:
        line = line.strip().split(': ')[1].split("|")
        
        current_numbs = []
        winning_numbs = []

        for index, elem in enumerate(line):
            elem = elem.replace(' ', ',').strip(',')
            elems = [int(x) for x in elem.split(',') if x]
            if index == 0: current_numbs = elems
            else: winning_numbs = elems

        correct_numbs = [numb for numb in current_numbs if numb in winning_numbs]

        if correct_numbs:
            points += 2**(len(correct_numbs)-1)

print(points)
