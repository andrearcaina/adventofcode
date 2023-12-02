sum = 0
string_values = {
    "one": "o1e", 
    "two": "t2o", 
    "three": "t3e", 
    "four": "f4r", 
    "five": "f5e", 
    "six": "s6x", 
    "seven": "s7n", 
    "eight": "e8t", 
    "nine": "n9e"
}

def replaceLine(line):
    for key, val in string_values.items():
        line = line.replace(key, val)

    return line

with open('day1.txt', 'r') as f:
    lines, digits = ["".join(line.split()) for line in f], []

    for line in lines:
        replaced_line = replaceLine(line)
        digits = [char for char in replaced_line if char.isdigit()]
        sum += int(digits[0]+digits[-1])

print(sum)
