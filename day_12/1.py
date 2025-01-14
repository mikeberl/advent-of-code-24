# Finding costs of gardens area with area x perimeter

file = 'input.txt'

with open(file, 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

cols = len(grid)
lines = len(grid[0])

sum = 0

assigned_blocks = []
for c in range(cols):
    for l in range(lines):
        if (c, l) not in assigned_blocks:
            assigned_blocks.append((c, l))
            region = [(c, l)]
            key = grid[c][l]  # Current block type
            end_region = []
            perimeter = 0
            while region:
                x, y = region.pop(0)
                end_region.append((x, y))

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= cols or ny < 0 or ny >= lines:
                        perimeter += 1
                    else :
                        if grid[nx][ny] != key:
                            perimeter += 1
                    if 0 <= nx < cols and 0 <= ny < lines:
                        if grid[nx][ny] == key and (nx, ny) not in assigned_blocks:
                            assigned_blocks.append((nx, ny))
                            region.append((nx, ny))

            area = len(end_region)

            print(f"Found region {key} with {area} blocks and perimeter {perimeter}")
            sum += area * perimeter
print("Result: ", sum)
