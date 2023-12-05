points = 0

with open('day4.txt', 'r') as f:
    for line in f:
        line = line.strip().split(': ')[1].split('|')
        
        current_numbs = {int(numb) for numb in line[0].split()}
        winning_numbs = {int(numb) for numb in line[1].split()}

        correct_numbs = current_numbs.intersection(winning_numbs)

        if correct_numbs:
            points += 2**(len(correct_numbs)-1)

print(points)
