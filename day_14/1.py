# Moving robots based on input file constrains and counting them at the end based on the area were they are located

# to move the robots before performing calculation of result
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

# debug function
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

# to perform final calculation and obtaining result
def calculate_quadrant_score(robots):
    half_x = map_x // 2
    half_y = map_y // 2
    
    quadrants = [0, 0, 0, 0]
    for (x, y), _ in robots:
        if y == half_y:
            continue
        
        if y < half_y: 
            if x < half_x:
                quadrants[1] += 1  
            elif x == half_x:
                continue
            else:    
                quadrants[0] += 1 
        else:  
            if x < half_x:
                quadrants[2] += 1 
            elif x == half_x:
                continue
            else:
                quadrants[3] += 1
    final_score = 1
    for count in quadrants:
        final_score *= count
        
    return final_score


file = "input.txt"
map_x, map_y = 101, 103
robots = []
with open(file, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            parti = line.split()
            p = tuple(map(int, parti[0][2:].split(',')))
            v = tuple(map(int, parti[1][2:].split(',')))
            robots.append((p, v))
moved_robots = move(robots, 100)
final_score = calculate_quadrant_score(moved_robots)
print("Result:", final_score)
