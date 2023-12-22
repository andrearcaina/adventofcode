OASIS = []
total = 0

def extrapolate(history):
    count = 0
    for i in range(len(history)):
        if history[i]:
            break
        count += 1
    
    if len(history) == count:
        return 0
    
    new_history = []
    for i in range(len(history)-1):
        new_history.append(history[i+1] - history[i])

    return history[-1] + extrapolate(new_history)

with open('day9.txt', 'r') as f:
    for line in f:
        line = line.strip()
        report = [int(val) for val in line.split()]
        OASIS.append(report)

    for report in OASIS:
        total += extrapolate(report)

print(total)