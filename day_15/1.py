# Moving a robot the move boxes around the map
# Result is the sum of all boxes GPS coordinates

def parse_input(filename):
    map_grid = []
    robot_position = None
    commands = []
    
    with open(filename, 'r') as file:
        for y, line in enumerate(file):
            line = line.strip()
            if len(line) > 0 and line[0] == '#' and len(line) > 1:
                map_grid.append(list(line))
                
                if '@' in line:
                    x = line.index('@')
                    robot_position = (x, y)
            
            elif len(line) > 0 and all(char in '<>v^' for char in line):
                commands.extend(list(line))
    
    return map_grid, robot_position, commands

def move(map_grid, robot_position, c):
    x, y = robot_position
    
    directions = {
        '^': (0, -1),  
        'v': (0, 1),  
        '<': (-1, 0), 
        '>': (1, 0) 
    }
    dx, dy = directions[c]
    new_x, new_y = x + dx, y + dy
    if (map_grid[new_y][new_x] == '.'):
        
        map_grid[y][x] = '.'
        
        map_grid[new_y][new_x] = '@'
        
        return map_grid, (new_x, new_y)
    
    elif map_grid[new_y][new_x] == 'O':

        current_x, current_y = new_x, new_y
        
        while map_grid[current_y][current_x] == 'O':
            current_x += dx
            current_y += dy
            
            if map_grid[current_y][current_x] == '.':
                break
            elif map_grid[current_y][current_x] == '#':
                return map_grid, robot_position
        map_grid[current_y][current_x] = 'O'
            
        map_grid[y][x] = '.'
        
        map_grid[new_y][new_x] = '@'
        
        return map_grid, (new_x, new_y)
            
    return map_grid, robot_position

filename = 'input.txt'

map_grid, robot_position, commands = parse_input(filename)


for c in commands:
    map_grid, robot_position = move(map_grid, robot_position, c)
    # print(f'After applying command {c}, map is:')
    # for row in map_grid:
    #         print(''.join(row))

result = 0
for row in range(len(map_grid)):
    for col in range(len(map_grid[0])):
        if map_grid[row][col] == 'O':
            result += row * 100 + col
print("Result: ", result)

