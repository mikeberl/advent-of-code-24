def check_loop(mappa):
    steps = 0
    while(True):
        if (steps > 100000): 
            return True
        if personaggio['direzione'] == '^':
            if personaggio['y'] - 1 < 0 :
                return False
            elif mappa[personaggio['y'] - 1][personaggio['x']] == 'U':
                return True
            elif mappa[personaggio['y'] - 1][personaggio['x']] != '#':
                personaggio['y'] -= 1
                steps += 1
            elif mappa[personaggio['y'] - 1][personaggio['x']] == '#':
                personaggio['direzione'] = '>'
                mappa[personaggio['y']][personaggio['x']] = 'U'

        elif personaggio['direzione'] == 'v':
            if personaggio['y'] + 1 >= len(mappa) :
                return False
            elif mappa[personaggio['y'] + 1][personaggio['x']] == 'D':
                return True
            if mappa[personaggio['y'] + 1][personaggio['x']] != '#':
                personaggio['y'] += 1
                steps += 1
            elif mappa[personaggio['y'] + 1][personaggio['x']] == '#':
                personaggio['direzione'] = '<'
                mappa[personaggio['y']][personaggio['x']] = 'D'

        elif personaggio['direzione'] == '>':
            if personaggio['x'] + 1 >= len(mappa[0]) :
                return False
            elif mappa[personaggio['y']][personaggio['x'] + 1] == 'R':
                return True
            if mappa[personaggio['y']][personaggio['x'] + 1] != '#':
                personaggio['x'] += 1
                steps += 1
            elif mappa[personaggio['y']][personaggio['x'] + 1] == '#':
                personaggio['direzione'] = 'v'
                mappa[personaggio['y']][personaggio['x']] = 'R'

        elif personaggio['direzione'] == '<':
            if personaggio['x'] - 1 < 0 :
                return False
            elif mappa[personaggio['y']][personaggio['x'] - 1] == 'L':
                return True

            if mappa[personaggio['y']][personaggio['x'] - 1 ] != '#':
                personaggio['x'] -= 1
                steps += 1
            elif mappa[personaggio['y']][personaggio['x'] - 1] == '#':
                personaggio['direzione'] = '^'
                mappa[personaggio['y']][personaggio['x']] = 'L'

with open('input.txt', 'r') as f:
    lines = f.readlines()

mappa = [list(line.strip()) for line in lines]

personaggio = None
for y, riga in enumerate(mappa):
    for x, cella in enumerate(riga):
        if cella in ['^', 'v', '<', '>']:
            personaggio = {'x': x, 'y': y, 'direzione': cella}
            break
    if personaggio:
        break


initial_x = personaggio['x']
initial_y = personaggio['y']


new_block_for_loop = 0

for l in range(len(mappa)):
    for c in range(len(mappa[0])):
        if (l == initial_y and c == initial_x) or mappa[l][c] == '#':
            continue
        
        new_map = [riga[:] for riga in mappa]
        
        new_map[l][c] = '#'
        
        personaggio['x'] = initial_x
        personaggio['y'] = initial_y
        personaggio['direzione'] = '^'
        
        if check_loop(new_map):
            new_block_for_loop += 1

print(f"Totale nuovi blocchi che creano loop: {new_block_for_loop}")