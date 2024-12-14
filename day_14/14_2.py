file = "input.txt"
map_x, map_y = 101, 103

def move(robots, seconds):
    for _ in range(seconds):
        for i in range(len(robots)):
            (px, py), (vx, vy) = robots[i]
            
            new_px = px + vx
            new_py = py + vy
            
            if new_px < 0:
                new_px += map_x
            elif new_px >= map_x:
                new_px -= map_x
            
            if new_py < 0:
                new_py += map_y
            elif new_py >= map_y:
                new_py -= map_y
            
            robots[i] = ((new_px, new_py), (vx, vy))
    return robots

def print_map(robots):
    map = [['.' for _ in range(map_x)] for _ in range(map_y)]

    count = {}

    for p, _ in robots:
        if p in count:
            count[p] += 1
        else:
            count[p] = 1

    for (x, y), count in count.items():
        if 0 <= x < map_x and 0 <= y < map_y:
            map[y][x] = str(count)

    for line in map:
        print(' '.join(line))

# seraching for 3 columns with 10 aligned robots
def check_alignment(robots):
    col_positions = {}
    
    for (x, y), _ in robots:
        if x not in col_positions:
            col_positions[x] = set()
        col_positions[x].add(y)
    
    aligned_columns = 0
    for col, positions in col_positions.items():
        consec_robots = 0
        max_consec_robots = 0
        prev_pos = None
        
        for pos in sorted(positions):
            if prev_pos is None or pos == prev_pos + 1:
                consec_robots += 1
            else:
                max_consec_robots = max(max_consec_robots, consec_robots)
                consec_robots = 1
            prev_pos = pos
        
        max_consec_robots = max(max_consec_robots, consec_robots)
        
        if max_consec_robots >= 10:
            aligned_columns += 1
    
    return aligned_columns >= 3

robots = []
with open(file, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            parti = line.split()
            p = tuple(map(int, parti[0][2:].split(',')))
            v = tuple(map(int, parti[1][2:].split(',')))
            robots.append((p, v))

moves = 0
while not check_alignment(robots):
    robots = move(robots, 1)
    moves += 1

print(f"Alignment found after {moves} moves:")
print_map(robots)