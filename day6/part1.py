with open('day6/input.txt', 'r') as f:
    lines = f.readlines()

    running_total = 0

    # Create a questions answered yes dict
    answered_yes = {}
    for line in lines:

        # Check if a new group
        if line == '\n':
            running_total += len(answered_yes.keys())
            print(answered_yes, running_total)
            answered_yes = {}
        
        else:
            for q in line.strip('\n'):
                if q in answered_yes.keys():
                    answered_yes[q] += 1
                else:
                    answered_yes[q] = 1


print(running_total)
        
