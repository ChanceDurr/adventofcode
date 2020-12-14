def trees_encountered(slope_right, slope_down):
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

pass1 = trees_encountered(1, 1)
pass2 = trees_encountered(3, 1)
pass3 = trees_encountered(5, 1)
pass4 = trees_encountered(7, 1)
pass5 = trees_encountered(1, 2)

print(pass1 * pass2 * pass3 * pass4 * pass5)
