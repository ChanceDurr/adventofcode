# Find two entries that sum to 2020 and then multiply them together
entries = []
with open('day1/input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        entries.append(int(line.strip('\n')))

found = False

for i in range(len(entries)):
    if found == True:
        break
    for j in range(len(entries)):
        if found == True:
            break
        for k in range(len(entries)):
            if found == True:
                break
            if i != j and i != k and j != k:
                if entries[i] + entries[j] + entries[k] == 2020:
                    print(entries[i] * entries[j] * entries[k])
                    found = True

            