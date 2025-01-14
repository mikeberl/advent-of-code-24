# Counting the numbers of valid antinodes placed in map based on antennas
# Other rules to place and count antinodes

with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

columns = len(grid)
rows = len(grid[0])
result = 0


for r1 in range(rows):
    for c1 in range(columns):
        if grid[r1][c1].isalpha() or grid[r1][c1].isdigit():
            ch = grid[r1][c1]
            for r2 in range(rows):
                for c2 in range(columns):

                    if (grid[r2][c2] == ch and (c1 != c2 or r1 != r2)):
                        mul = 1
                        add_r = r2 - r1
                        add_c = c2 - c1
                        while (r2 + add_r * mul >= 0 and r2 + add_r * mul < rows and c2 + add_c *mul >= 0 and c2 + add_c * mul < columns):
                            if not grid[r2 + add_r * mul][c2 + add_c * mul].isalpha() and not grid[r2 + add_r * mul][c2 + add_c * mul].isdigit() and grid[r2 + add_r * mul][c2 + add_c * mul] != '#':
                                grid[r2 + add_r * mul][c2 + add_c * mul] = '#'                   
                            mul += 1
                            

for r1 in range(rows):
    for c1 in range(columns):
        if grid[r1][c1] == '#':
            result += 1
        #counting letters only if not unique
        elif grid[r1][c1].isalpha() or grid[r1][c1].isdigit():
            stop = False
            for r2 in range(rows):
                if stop:
                    break
                for c2 in range(columns):
                    if (grid[r2][c2] == ch and (c1 != c2 or r1 != r2)):
                        result += 1
                        stop = True
                        break

print(f'Result: {result}')
