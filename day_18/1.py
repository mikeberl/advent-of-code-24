# Populating a maze with obstacles (only the first kilobyte of obstacles in the input file) 
# and finding the shortest path from the top left corner to the bottom right corner

import heapq

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
        visited = set()

        while pq:
            cost, current = heapq.heappop(pq)

            if current in visited:
                continue
            visited.add(current)

            if current == end:
                return cost

            x, y = current

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    new_cost = cost + 1
                    if (nx, ny) not in distances or new_cost < distances[(nx, ny)]:
                        distances[(nx, ny)] = new_cost
                        heapq.heappush(pq, (new_cost, (nx, ny)))

        return -1

file_name = "input.txt"
with open(file_name, "r") as file:
    lines = file.readlines()

grid = [["." for _ in range(71)] for _ in range(71)]

for l in range(1024):
    x, y = map(int, lines[l].strip().split(","))
    grid[y][x] = "#" 

for row in grid:
    print("".join(row))
solver = MazeSolver(grid)
start = (0, 0)  
end = (70, 70) 
shortest_path_cost = solver.find_shortest_path(start, end)

print(f"Il costo del percorso più corto è: {shortest_path_cost}")
