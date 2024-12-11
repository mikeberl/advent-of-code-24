file = "input.txt"

def trova_path_complete(grid):
    lines, cols = len(grid), len(grid[0])
    
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    def valid(r, c):
        return 0 <= r < lines and 0 <= c < cols
    
    def find_path(start_r, start_c):
        pos = {0: {(start_r, start_c)}}
        
        end_points = set()
        
        for key in range(9):
            new_pos = set()
            
            for r, c in pos[key]:
                for dir_l, dir_c in direction:
                    new_line, new_col = r + dir_l, c + dir_c
                    
                    if (valid(new_line, new_col) and 
                        grid[new_line][new_col] == str(key + 1)):
                        new_pos.add((new_line, new_col))
            
            if not new_pos:
                break
            
            pos[key + 1] = new_pos
            
            if key == 8:
                end_points.update(new_pos)
        
        return len(end_points)
    
    zeros = [(r, c) for r in range(lines) for c in range(cols) if grid[r][c] == '0']
    
    path_sum = sum(find_path(r, c) for r, c in zeros)
    
    return path_sum



with open(file, "r") as file:
    grid = [list(line.strip()) for line in file if line.strip()]



result = trova_path_complete(grid)
print(f"\nResult: {result}")

