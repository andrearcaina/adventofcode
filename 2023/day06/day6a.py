times = []
distances = []
err = 1 

with open('day6.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith("Time:"):
            values = [int(val) for val in line.split()[1:]]
            times.extend(values)
        elif line.startswith("Distance:"):
            values = [int(val) for val in line.split()[1:]]
            distances.extend(values)

    for time, distance in zip(times, distances):
        margin = 0
        for hold in range(time):
            if hold * (time - hold) > distance:
                margin += 1
        err *= margin

print(err)