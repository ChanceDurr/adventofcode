# Iterate through each password to check if it is valid
valid = 0

with open('day2/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        password = line.split(':')[1].strip(' ')
        req_letter = line.split(' ')[1].strip(':')
        req_range_a = int(line.split(' ')[0].split('-')[0])
        req_range_b = int(line.split(' ')[0].split('-')[1])

        # Check if letter is in password certain amount of times
        if password.count(req_letter) in range(req_range_a, req_range_b + 1):
            valid += 1

print(valid)