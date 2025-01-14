# Counting steps the guard is doing before leaving the map

with open('input.txt', 'r') as f:
    lines = f.readlines()
map = [list(line.strip()) for line in lines]

guard = None
for y, line in enumerate(map):
    for x, col in enumerate(line):
        if col in ['^', 'v', '<', '>']:
            guard = {'x': x, 'y': y, 'dir': col}
            map[y][x] = 'X'
            break
    if guard:
        break


steps = 1
while(True):
    if guard['dir'] == '^':
        if guard['y'] - 1 >= len(map) or guard['x'] >= len(map[0]):
            break
        elif map[guard['y'] - 1][guard['x']] != '#':
            guard['y'] -= 1
            if map[guard['y']][guard['x']] != 'X':
                map[guard['y']][guard['x']] = 'X'
                steps += 1
        elif map[guard['y'] - 1][guard['x']] == '#':
            guard['dir'] = '>'
        else:
            break
    elif guard['dir'] == 'v':
        if guard['y'] + 1 >= len(map) or guard['x'] >= len(map[0]):
            break
        elif map[guard['y'] + 1][guard['x']] != '#':
            guard['y'] += 1
            if map[guard['y']][guard['x']] != 'X':
                map[guard['y']][guard['x']] = 'X'
                steps += 1

        elif map[guard['y'] + 1][guard['x']] == '#':
            guard['dir'] = '<'
        else:
            break
    elif guard['dir'] == '>':
        if guard['y'] >= len(map) or guard['x'] + 1 >= len(map[0]):
            break
        elif map[guard['y']][guard['x'] + 1] != '#':
            guard['x'] += 1
            if map[guard['y']][guard['x']] != 'X':
                map[guard['y']][guard['x']] = 'X'
                steps += 1
        elif map[guard['y']][guard['x'] + 1] == '#':
            guard['dir'] = 'v'
        else:
            break
    elif guard['dir'] == '<':
        if guard['y'] >= len(map) or guard['x'] - 1 >= len(map[0]):
            break
        elif map[guard['y']][guard['x'] - 1 ] != '#':
            guard['x'] -= 1
            if map[guard['y']][guard['x']] != 'X':
                map[guard['y']][guard['x']] = 'X'
                steps += 1
        elif map[guard['y']][guard['x'] - 1] == '#':
            guard['dir'] = '^'

            
map[guard['y']][guard['x']] = 'U'
print("Result: ", steps)



