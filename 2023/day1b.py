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
    lines = []
    string = ''

    for line in f:
        line_split = "".join(line.split())
        lines.append(line_split)

    for line in lines:
        line = replaceLine(line)
        
        for char in line:
            if char.isdigit():
                string += char
        
        sum += int(string[0]+string[-1])
        string = ''

print(sum)
