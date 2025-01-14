#Counting the amount of blocks that can be placed to create an infinite loop

def check_loop(map):
    steps = 0
    while(True):
        if (steps > 100000): 
            return True
        if guard['dir'] == '^':
            if guard['y'] - 1 < 0 :
                return False
            elif map[guard['y'] - 1][guard['x']] == 'U':
                return True
            elif map[guard['y'] - 1][guard['x']] != '#':
                guard['y'] -= 1
                steps += 1
            elif map[guard['y'] - 1][guard['x']] == '#':
                guard['dir'] = '>'
                map[guard['y']][guard['x']] = 'U'

        elif guard['dir'] == 'v':
            if guard['y'] + 1 >= len(map) :
                return False
            elif map[guard['y'] + 1][guard['x']] == 'D':
                return True
            if map[guard['y'] + 1][guard['x']] != '#':
                guard['y'] += 1
                steps += 1
            elif map[guard['y'] + 1][guard['x']] == '#':
                guard['dir'] = '<'
                map[guard['y']][guard['x']] = 'D'

        elif guard['dir'] == '>':
            if guard['x'] + 1 >= len(map[0]) :
                return False
            elif map[guard['y']][guard['x'] + 1] == 'R':
                return True
            if map[guard['y']][guard['x'] + 1] != '#':
                guard['x'] += 1
                steps += 1
            elif map[guard['y']][guard['x'] + 1] == '#':
                guard['dir'] = 'v'
                map[guard['y']][guard['x']] = 'R'

        elif guard['dir'] == '<':
            if guard['x'] - 1 < 0 :
                return False
            elif map[guard['y']][guard['x'] - 1] == 'L':
                return True

            if map[guard['y']][guard['x'] - 1 ] != '#':
                guard['x'] -= 1
                steps += 1
            elif map[guard['y']][guard['x'] - 1] == '#':
                guard['dir'] = '^'
                map[guard['y']][guard['x']] = 'L'

with open('input.txt', 'r') as f:
    lines = f.readlines()

map = [list(line.strip()) for line in lines]

guard = None
for y, line in enumerate(map):
    for x, col in enumerate(line):
        if col in ['^', 'v', '<', '>']:
            guard = {'x': x, 'y': y, 'dir': col}
            break
    if guard:
        break


initial_x = guard['x']
initial_y = guard['y']


new_block_for_loop = 0

for l in range(len(map)):
    for c in range(len(map[0])):
        if (l == initial_y and c == initial_x) or map[l][c] == '#':
            continue
        
        new_map = [riga[:] for riga in map]
        
        new_map[l][c] = '#'
        
        guard['x'] = initial_x
        guard['y'] = initial_y
        guard['dir'] = '^'
        
        if check_loop(new_map):
            new_block_for_loop += 1

print(f"New blocks creating an infinite loop: {new_block_for_loop}")