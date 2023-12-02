sum = 0

with open('day1.txt', 'r') as f:
    for line in f:
        digits = [char for char in line if char.isdigit()]

        digit = digits[0]+digits[-1]
        sum += int(digit)

print(sum)
