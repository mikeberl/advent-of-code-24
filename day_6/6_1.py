with open('input.txt', 'r') as f:
    lines = f.readlines()
map = [list(line.strip()) for line in lines]

personaggio = None
for y, riga in enumerate(map):
    for x, cella in enumerate(riga):
        if cella in ['^', 'v', '<', '>']:
            personaggio = {'x': x, 'y': y, 'direzione': cella}
            map[y][x] = 'X'
            break
    if personaggio:
        break


steps = 1
while(True):
    if personaggio['direzione'] == '^':
        if personaggio['y'] - 1 >= len(map) or personaggio['x'] >= len(map[0]):
            break
        elif map[personaggio['y'] - 1][personaggio['x']] != '#':
            personaggio['y'] -= 1
            if map[personaggio['y']][personaggio['x']] != 'X':
                map[personaggio['y']][personaggio['x']] = 'X'
                steps += 1
        elif map[personaggio['y'] - 1][personaggio['x']] == '#':
            personaggio['direzione'] = '>'
        else:
            break
    elif personaggio['direzione'] == 'v':
        if personaggio['y'] + 1 >= len(map) or personaggio['x'] >= len(map[0]):
            break
        elif map[personaggio['y'] + 1][personaggio['x']] != '#':
            personaggio['y'] += 1
            if map[personaggio['y']][personaggio['x']] != 'X':
                map[personaggio['y']][personaggio['x']] = 'X'
                steps += 1

        elif map[personaggio['y'] + 1][personaggio['x']] == '#':
            personaggio['direzione'] = '<'
        else:
            break
    elif personaggio['direzione'] == '>':
        if personaggio['y'] >= len(map) or personaggio['x'] + 1 >= len(map[0]):
            break
        elif map[personaggio['y']][personaggio['x'] + 1] != '#':
            personaggio['x'] += 1
            if map[personaggio['y']][personaggio['x']] != 'X':
                map[personaggio['y']][personaggio['x']] = 'X'
                steps += 1
        elif map[personaggio['y']][personaggio['x'] + 1] == '#':
            personaggio['direzione'] = 'v'
        else:
            break
    elif personaggio['direzione'] == '<':
        if personaggio['y'] >= len(map) or personaggio['x'] - 1 >= len(map[0]):
            break
        elif map[personaggio['y']][personaggio['x'] - 1 ] != '#':
            personaggio['x'] -= 1
            if map[personaggio['y']][personaggio['x']] != 'X':
                map[personaggio['y']][personaggio['x']] = 'X'
                steps += 1
        elif map[personaggio['y']][personaggio['x'] - 1] == '#':
            personaggio['direzione'] = '^'

            
map[personaggio['y']][personaggio['x']] = 'U'
print("Result: ", steps)



