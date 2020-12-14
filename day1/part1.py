# Find two entries that sum to 2020 and then multiply them together
entries = []
with open('day1/input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        entries.append(int(line.strip('\n')))

for i in range(len(entries)):
    for j in range(len(entries)):
        if i != j:
            if entries[i] + entries[j] == 2020:
                print(entries[i] * entries[j])
                break

            