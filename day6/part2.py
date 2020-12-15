with open('day6/input.txt', 'r') as f:
    lines = f.readlines()

    running_total = 0
    group_size = 0

    # Create a questions answered yes dict
    answered_yes = {}
    for line in lines:

        # Check if a new group
        if line == '\n':
            for key, value in answered_yes.items():
                if value == group_size:
                    running_total += 1
            
            answered_yes = {}
            group_size = 0
        
        else:
            group_size += 1

            for q in line.strip('\n'):
                if q in answered_yes.keys():
                    answered_yes[q] += 1
                else:
                    answered_yes[q] = 1


print(running_total)
        
