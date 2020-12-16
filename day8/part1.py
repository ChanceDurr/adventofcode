instructions = {}

with open('day8/input.txt', 'r') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        instructions[count] = (line.split()[0], int(line.split()[1]))
        count += 1

cur = 0
visited = []
acc = 0
while cur not in visited:
    visited.append(cur)

    if instructions[cur][0] == 'jmp':
        cur += instructions[cur][1]
    if instructions[cur][0] == 'acc':
        acc += instructions[cur][1]
        cur += 1
    if instructions[cur][0] == 'nop':
        cur += 1

print(acc)