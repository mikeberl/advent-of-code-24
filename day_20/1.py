# Given a maze with a starting point (S) and a end point (E) find how many times
# during the path we can skip a single wall to save at least 100 steps

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
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    def is_valid(x, y):
        return 0 <= x < cols and 0 <= y < rows

    big_jumps = []

    for i, (x, y) in enumerate(path):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                for j in range(i + 101, len(path)):
                    if path[j] == (nx, ny):
                        steps_skipped = j - i 
                        big_jumps.append((x, y, nx, ny, j, steps_skipped - 2))
                        break

    return big_jumps
    

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

for row in grid:
    print("".join(row))
solver = MazeSolver(grid)
cost, path = solver.find_shortest_path(start, end)

if cost != -1:
    print(f"Costo: {cost}")
    big_jumps = find_big_jumps(path, grid)
    print(len(big_jumps))
else:
    print("Nessun percorso trovato.")
