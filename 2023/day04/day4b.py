copies = {}

with open('day4.txt', 'r') as f:
    for index, line in enumerate(f):
        # copies = {'Card #1': 1} 
        # key = card #, value = number of copies of that card
        card_num = index+1
        CARD = 'Card #'+str(card_num)
        if CARD not in copies:
            copies[CARD] = 1

        line = line.strip().split(': ')[1].split('|')
        
        current_numbs = {int(numb) for numb in line[0].split()}
        winning_numbs = {int(numb) for numb in line[1].split()}

        correct_numbs = current_numbs.intersection(winning_numbs)
        matching = len(correct_numbs)

        # for first line, which is CARD #1
        # {41, 48, 83, 86, 17} and {83, 86, 6, 31, 17, 9, 48, 53}
        # basically, from card_num+1 which is the next card, so CARD #2 to CARD #2 + total matching numbers
        # so, CARD #2 + 4 (since there are 4 matching numbers) = CARD #6, but range is exclusive, so to CARD #5
        # then get the value of CARD #2, otherwise return 1 if it doesn't exist and add it the value of CARD #1
        # it then iterates again when done
        for num in range(card_num + 1, card_num + 1 + matching):
            card = 'Card #'+str(num)
            copies[card] = copies.get(card, 1) + copies[CARD]

print(sum(copies.values()))