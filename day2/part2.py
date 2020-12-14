# Iterate through each password to check if it is valid
valid = 0

with open('day2/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        password = line.split(':')[1].strip(' ')
        req_letter = line.split(' ')[1].strip(':')

        # Subtract one to make up for nonzero index
        req_range_a = int(line.split(' ')[0].split('-')[0]) - 1
        req_range_b = int(line.split(' ')[0].split('-')[1]) - 1

        # Check if letter is in only 1 spot
        if password[req_range_a] == req_letter or password[req_range_b] == req_letter:
            if password[req_range_a] == req_letter and password[req_range_b] == req_letter:
                pass
            else:
                valid += 1

print(valid)