instructions = {}

with open('day8/input.txt', 'r') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        instructions[count] = (line.split()[0], int(line.split()[1]))
        count += 1

og = instructions
instructions_switched = []
finished = False


# Run until its able to complete while switching out instructions
while finished == False:
    cur = 0
    acc = 0
    visited = []
    switched = False

    # Run the program until complete unless it starts to loop
    while cur not in visited and cur <= 625:

        visited.append(cur)
        if instructions[cur][0] == 'jmp':
            if cur not in instructions_switched and not switched:
                instructions_switched.append(cur)
                switched = True
                cur += 1
            else:
                cur += instructions[cur][1]
        elif instructions[cur][0] == 'acc':
            acc += instructions[cur][1]
            cur += 1
        elif instructions[cur][0] == 'nop':
            if cur not in instructions_switched and not switched:
                instructions_switched.append(cur)
                switch = True
                cur += instructions[cur][1]
            else:
                cur += 1
    if cur == 626:
        finished = True
        print(acc)

    # Switch back to original instructions
    instructions = og

                
                


