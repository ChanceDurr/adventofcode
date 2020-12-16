rules = {}

# Create a neat dictionary of the rules
with open('day7/input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        parent = line.split('bags contain')[0].strip()
        children = line.split('bags contain')[1].split(',')
        children = [child.strip('\n').strip('.').strip('bags').strip() for child in children]
        # children = [' '.join(child.split()[1:]) for child in children]
        child_dict = {}
        for child in children:
            if child.split()[0] != 'no':
                child_dict[' '.join(child.split()[1:])] = int(child.split()[0])

                rules[parent] = child_dict


# Recursivly get the bag
def get_children(parent, multiplier):
    count = 0
    for child, value in rules[parent].items():
        count += value * multiplier
        if child in rules.keys():
            count += get_children(child, value * multiplier)

    return count

# Input for our shiny gold bag
print(get_children('shiny gold', 1))