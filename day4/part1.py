passports = {}

with open('day4/input.txt', 'r') as f:
    count = 0
    for line in f.readlines():
        has_fields = []
        if line == '\n':
            count += 1
            continue

        else:
            line = line.strip('\n')
            fields = line.split(' ')

            # Check if there is already a list of fields, if not, add empty list
            if count not in passports.keys():
                passports[count] = []

            for field in fields:
                passports[count].append(field.split(':')[0])

valid = 0
requirments = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for fields in passports.values():
    print(fields)
    if all(req in fields for req in requirments):
        valid += 1
        print('PASS\n')



print(valid)