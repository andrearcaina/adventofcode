total = 0
hands = []
card_values = {
    "T": "A", 
    "J": "B", 
    "Q": "C", 
    "K": "D", 
    "A": "E"
}

def strength(hand):
    counts = [hand.count(card) for card in hand]
    return sum(counts), [card_values.get(card, card) for card in hand]

with open('day7.txt', 'r') as f:
    for line in f:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

hands.sort(key=lambda hands:strength(hands[0]))

for rank, (hand, bid) in enumerate(hands):
    total += bid * (rank + 1)

print(total)
