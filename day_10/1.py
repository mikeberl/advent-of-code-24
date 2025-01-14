# Counting all possible way to reach point 9 from all the possible point 1 in a 2D-map
# 1 -> to many 9, but just one way for every 1-9

def find_complete_paths(grid):
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

def load_grid(filename):
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file if line.strip()]

def main():
    grid = load_grid("input.txt")
    
    result = find_complete_paths(grid)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()



