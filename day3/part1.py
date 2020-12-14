def trees_encountered(slope_down, slope_right):
    trees_encountered = 0
    cur_x = 0
    cur_y = 0

    map = {}

    with open("day3/input.txt", 'r') as f:
        line_num = 0
        for line in f.readlines():
            map[line_num] = line.strip('\n')
            line_num += 1

    for line, row in map.items():
        if line % slope_down == 0:
            if row[cur_x % len(row)] == '#':
                trees_encountered += 1
            cur_x += slope_right
    
    return trees_encountered

print(trees_encountered(1, 3))
