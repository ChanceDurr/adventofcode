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
                passports[count] = {}

            for field in fields:
                passports[count][field.split(':')[0]] = field.split(':')[1]

valid = 0
requirments = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passport in passports.values():
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    if all(req in passport.keys() for req in requirments):

        # Check Birth Year 1920-2002
        if 1920 <= int(passport['byr']) <= 2002 and len(passport['byr']) == 4:
            byr = True
        
        # Check if Issue Year between 2010-2020
        if 2010 <= int(passport['iyr']) <= 2020 and len(passport['iyr']) == 4:
            iyr = True

        # Check if Exp Year in 2020-2030
        if 2020 <= int(passport['eyr']) <= 2030 and len(passport['eyr']) == 4:
            eyr = True

        # Check for correct height
        if passport['hgt'][-2:] == "cm":
            if 150 <= int(passport['hgt'][:-2]) <= 193:
                hgt = True
        elif passport['hgt'][-2:] == "in":
            if 59 <= int(passport['hgt'][:-2]) <= 76:
                hgt = True

        # Check for Hair color
        check = True
        if passport['hcl'][0] == '#' and len(passport['hcl']) == 7:
            for char in passport['hcl'][1:]:
                if char.isnumeric() is False:
                    if char > 'f':
                        check = False
                    

            if check:
                hcl = True
        
        # Check for eye color
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if any(color in passport['ecl'] for color in colors):
            ecl = True

        # Check if Passport id is nine digit num
        if len(passport['pid']) == 9 and passport['pid'].isnumeric():
            pid = True
            
        if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
            valid += 1

print(valid)