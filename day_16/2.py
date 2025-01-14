# Find the shortest path from S (start) to E (end) in the maze provided
# As there are many "shortest path" count all the blocks beeing part of one
# of these shortest paths

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

    def find_paths(self, start, end):
        start_state = (start[0], start[1], 0)
        
        heap = [(0, start_state, [start_state])]
        visited = {}
        min_cost = float('inf')
        all_min_paths = []
        
        while heap:
            total_cost, current, path = heappop(heap)
            
            if total_cost > min_cost:
                break
            
            cy, cx, current_dir = current
            
            if (cy, cx) == end:
                if total_cost < min_cost:
                    min_cost = total_cost
                    all_min_paths = [path]
                elif total_cost == min_cost:
                    all_min_paths.append(path)
                continue
            
            state_key = (cy, cx, current_dir)
            
            if (state_key not in visited or 
                total_cost <= visited[state_key]): # !
                visited[state_key] = total_cost
            else:
                continue
            
            for new_dir, (dy, dx) in enumerate(self.directions):
                ny, nx = cy + dy, cx + dx
                
                if not self.is_valid_move(ny, nx):
                    continue
                
                move_cost = 1
                rotation_cost = 1000 if abs(current_dir - new_dir) != 0 else 0
                new_total_cost = total_cost + move_cost + rotation_cost
                
                if new_total_cost <= min_cost:
                    new_path = path + [(ny, nx, new_dir)]
                    
                    heappush(heap, (
                        new_total_cost, 
                        (ny, nx, new_dir), 
                        new_path
                    ))
        
        return all_min_paths

def read_maze_from_file(filename):
    with open(filename, 'r') as f:
        maze_lines = f.readlines()
    
    maze = np.array([list(line.strip()) for line in maze_lines])
    
    start = tuple(np.argwhere(maze == 'S')[0])
    end = tuple(np.argwhere(maze == 'E')[0])
    
    return maze, start, end

def count_unique_cells(maze, paths):
    unique_cells = set()
    
    for path in paths:
        for y, x, _ in path:
            unique_cells.add((y, x))
    
    return len(unique_cells)

filename = "input.txt"
maze, start, end = read_maze_from_file(filename)
solver = MazeSolver(maze)
paths = solver.find_paths(start, end)
unique_cells_count = count_unique_cells(maze, paths)
print(f"Result: {unique_cells_count}")

