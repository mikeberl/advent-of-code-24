# Given a maze with a starting point (S) and a end point (E) find how many times
# during the path we can skip 2 consecutive walls to save at least 100 steps

import heapq
from collections import deque

class MazeSolver:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows and self.grid[y][x] != "#"

    def find_shortest_path(self, start, end):
        pq = []
        heapq.heappush(pq, (0, start))
        distances = {start: 0}
        previous = {start: None}
        visited = set()

        while pq:
            cost, current = heapq.heappop(pq)

            if current in visited:
                continue
            visited.add(current)

            if current == end:
                path = []
                while current:
                    path.append(current)
                    current = previous[current]
                path.reverse()
                return cost, path

            x, y = current

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    new_cost = cost + 1
                    if (nx, ny) not in distances or new_cost < distances[(nx, ny)]:
                        distances[(nx, ny)] = new_cost
                        previous[(nx, ny)] = current
                        heapq.heappush(pq, (new_cost, (nx, ny)))

        return -1, []
    
def find_big_jumps(path, grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Create a lookup dictionary for path points
    path_lookup = {(x, y): idx for idx, (x, y) in enumerate(path)}
    
    def is_valid(x, y):
        return 0 <= x < cols and 0 <= y < rows
    
    def find_jumps_from_point(start_x, start_y, start_idx):
        jumps = []
        queue = [(start_x, start_y, 0)]  # (x, y, steps_taken)
        visited = {(start_x, start_y): 0}
        
        while queue:
            x, y, steps = queue.pop(0)
            
            if steps > 20:  # Max steps limit
                continue
            
            # Check if current point is in path and would save steps
            if (x, y) in path_lookup:
                end_idx = path_lookup[(x, y)]
                if end_idx >= start_idx + 100:
                    steps_saved = end_idx - start_idx - steps
                    if steps_saved >= 100:
                        jumps.append((
                            start_x, start_y,
                            x, y,
                            end_idx,
                            steps_saved,
                            steps
                        ))
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    new_steps = steps + 1
                    if (nx, ny) not in visited or visited[(nx, ny)] > new_steps:
                        visited[(nx, ny)] = new_steps
                        queue.append((nx, ny, new_steps))
        
        return jumps
    
    big_jumps = []
    processed_starts = set()

    for i in range(0, len(path) - 100):
        start_x, start_y = path[i]
        if (start_x, start_y) not in processed_starts:
            processed_starts.add((start_x, start_y))
            big_jumps.extend(find_jumps_from_point(start_x, start_y, i))
    
    return big_jumps

def analyze_jumps(path, grid):
    big_jumps = find_big_jumps(path, grid)
    
    jump_counts = {}
    
    for jump in big_jumps:
        steps_saved = jump[5]
        jump_counts[steps_saved] = jump_counts.get(steps_saved, 0) + 1
    
    print(f"Here are the quantities of cheats in this example that save *50 picoseconds or more*:")
    for steps_saved in sorted(jump_counts.keys()):
        count = jump_counts[steps_saved]
        print(f"* There are {count} cheats that save {steps_saved} picoseconds.")
    
    return len(big_jumps)

file_name = "input.txt"
start = (0, 0)
end = (0, 0)

with open(file_name, "r") as file:
    grid = []
    for y, line in enumerate(file):
        row = list(line.strip())
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            elif cell == "E":
                end = (x, y)
        grid.append(row)

solver = MazeSolver(grid)
cost, path = solver.find_shortest_path(start, end)

if cost != -1:
    print(f"Cost: {cost}")
    total_jumps = analyze_jumps(path, grid)
    print(total_jumps)
