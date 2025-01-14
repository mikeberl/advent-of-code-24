# Find the shortest path from S (start) to E (end) in the maze provided
# Result is based on how many steps (1 point) + how many 90 degree rotations (1000 points) are performed

from heapq import heappush, heappop
import numpy as np

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows, self.cols = maze.shape
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def is_valid_move(self, y, x):
        return (0 <= y < self.rows and 
                0 <= x < self.cols and 
                self.maze[y, x] != '#')

    
    def find_path(self, start, end):
        start_state = (start[0], start[1], 0)
        
        heap = [(0, start_state, [start_state])] # (costo totale, stato, percorso)
        visited = set()
        
        while heap:
            total_cost, current, path = heappop(heap)
            
            cy, cx, current_dir = current
            
            if (cy, cx) == end:
                return path
            
            state_key = (cy, cx, current_dir)
            if state_key in visited:
                continue
            visited.add(state_key)
            
            for new_dir, (dy, dx) in enumerate(self.directions):
                ny, nx = cy + dy, cx + dx
                
                if not self.is_valid_move(ny, nx):
                    continue
                
                move_cost = 1
                rotation_cost = 1000 if abs(current_dir - new_dir) != 0 else 0
                new_total_cost = total_cost + move_cost + rotation_cost
                
                new_path = path + [(ny, nx, new_dir)]
                
                heappush(heap, (
                    new_total_cost, 
                    (ny, nx, new_dir), 
                    new_path
                ))
        
        return None

def read_maze_from_file(filename):
    with open(filename, 'r') as f:
        maze_lines = f.readlines()
    
    maze = np.array([list(line.strip()) for line in maze_lines])
    
    start = tuple(np.argwhere(maze == 'S')[0])
    end = tuple(np.argwhere(maze == 'E')[0])
    
    return maze, start, end


filename = "input.txt"
maze, start, end = read_maze_from_file(filename)
solver = MazeSolver(maze)
path = solver.find_path(start, end)

rotation_cost = sum(1000 for i in range(1, len(path)) if path[i][2] != path[i-1][2])
move_cost = len(path) - 1
total_cost = move_cost + rotation_cost

print(f"Result: {total_cost}")
