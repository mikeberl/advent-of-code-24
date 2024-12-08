with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

columns = len(grid)
rows = len(grid[0])
result = 0

# to count overlapping #
overlapping = 0
for r1 in range(rows):
    for c1 in range(columns):
        if grid[r1][c1].isalpha() or grid[r1][c1].isdigit():
            
            ch = grid[r1][c1]
            for r2 in range(rows):
                for c2 in range(columns):
                    if (grid[r2][c2] == ch and (c1 != c2 or r1 != r2)):
                        
                        # print(f'Character {ch}, found at {r2, c2}, {r1, c1}')
                        add_r = r2 - r1
                        add_c = c2 - c1
                        if (r2 + add_r >= 0 and r2 + add_r < rows and c2 + add_c >= 0 and c2 + add_c < columns):
                            if not grid[r2 + add_r][c2 + add_c].isalpha() and not grid[r2 + add_r][c2 + add_c].isdigit():
                                grid[r2 + add_r][c2 + add_c] = '#'
                            else:
                                overlapping += 1


for r1 in range(rows):
    for c1 in range(columns):
        if grid[r1][c1] == '#':
            result += 1
print(f'Result: {result + overlapping}')