# to find sides based on direction
def count_consecutive_block_series(blocks, direction):
    groups = {}
    
    for block in blocks:
        key = block[0] if direction == 'x' else block[1]
        if key not in groups:
            groups[key] = set()
        groups[key].add(block[1] if direction == 'x' else block[0])
    
    consecutive_series = 0
    
    for key, values in groups.items():
        sorted_values = sorted(list(values))
        
        i = 0
        while i < len(sorted_values):
            consecutive_series += 1
            
            current = sorted_values[i]
            while i < len(sorted_values) and sorted_values[i] == current:
                i += 1
                current += 1
    
    return consecutive_series

def get_direction(dx, dy):
    if dx == -1 and dy == 0:
        return 'up'
    elif dx == 1 and dy == 0:
        return 'down'
    elif dx == 0 and dy == -1:
        return 'right'
    elif dx == 0 and dy == 1:
        return 'left'
    
def find_cost(grid):

    sum = 0
    cols = len(grid)
    lines = len(grid[0])
    assigned_blocks = [] # for blocks that are already assigned to a region
    for c in range(cols):
        for l in range(lines):
            if (c, l) not in assigned_blocks:
                assigned_blocks.append((c, l))
                region = [(c, l)]
                key = grid[c][l] 
                end_region = []
                while region:
                    x, y = region.pop(0)
                    end_region.append((x, y))

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < cols and 0 <= ny < lines:
                            if grid[nx][ny] == key and (nx, ny) not in assigned_blocks:
                                assigned_blocks.append((nx, ny))
                                region.append((nx, ny))

                area = len(end_region)
                
                external_blocks = {
                    'up': [],
                    'down': [],
                    'left': [], 
                    'right': []
                } # to find the externality direction of every block                
                while end_region:
                    x, y = end_region.pop(0)
                    directions = []
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy                        
                        if nx < 0 or nx >= cols or ny < 0 or ny >= lines:
                            directions.append(get_direction(dx, dy))                        
                        elif 0 <= nx < cols and 0 <= ny < lines:
                            if grid[nx][ny] != key:
                                directions.append(get_direction(dx, dy))  
                                                      
                    for direction in directions:
                        if (x, y) not in external_blocks[direction]:
                            external_blocks[direction].append((x, y))

                sides = ( count_consecutive_block_series(external_blocks['up'], 'x') 
                    + count_consecutive_block_series(external_blocks['down'], 'x') 
                    + count_consecutive_block_series(external_blocks['right'], 'y') 
                    + count_consecutive_block_series(external_blocks['left'], 'y') 
                )
                sum += area * sides
    return sum


file = 'input.txt'

with open(file, 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]


print("Result: ", find_cost(grid))
