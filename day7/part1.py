bags = {}

with open('day7/input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        parent = line.split('bags contain')[0].strip()
        children = line.split('bags contain')[1].split(',')
        children = [child.strip('\n').strip('.').strip('bags').strip() for child in children]
        children = [' '.join(child.split()[1:]) for child in children]

        if children != ['other']:
            bags[parent] = children


def check_for_parents(child_bags):
    new_list = []
    # For each bag rule
    for parent, children in bags.items():
        # For each bag that can hold ours directly
        for bag in child_bags:
            # Check if bag is in the children on rule
            if bag in children:
                # Append to our list if not in there already
                if parent not in new_list:
                    new_list.append(parent)
    
    # If parents, check for their parents, else return the new_list with the old list
    if new_list:
        return check_for_parents(new_list) + child_bags
    else:
        return new_list + child_bags


print(len(set(check_for_parents(["shiny gold"]))) - 1)


