# Counting all possible way to reach point 9 from all the possible point 1 in a 2D-map
# 1 -> to many 9, for every 1 to 9 count all the possible ways to reach that 9

def find_complete_paths(grid):
    rows, cols = len(grid), len(grid[0])
    
    DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def explore_paths(start_row, start_col):
        current_paths = [[(start_row, start_col)]]
        
        for target_number in range(1, 10):
            new_paths = []
            
            for path in current_paths:
                current_positions = [path[-1]]
                path_extended = False
                
                for row, col in current_positions:
                    for d_row, d_col in DIRECTIONS:
                        new_row, new_col = row + d_row, col + d_col
                        
                        if (is_valid_position(new_row, new_col) and 
                            grid[new_row][new_col] == str(target_number)):
                            extended_path = path.copy()
                            extended_path.append((new_row, new_col))
                            new_paths.append(extended_path)
                            path_extended = True
                
                if not path_extended:
                    new_paths.append(path)
            
            current_paths = new_paths
            
            if not current_paths:
                break
        
        return current_paths
    
    start_positions = [(r, c) for r in range(rows) 
                       for c in range(cols) if grid[r][c] == '0']
    
    total_complete_paths = 0
    zero_path_results = []
    
    for start_pos in start_positions:
        found_paths = explore_paths(*start_pos)
        
        complete_paths = [path for path in found_paths if len(path) == 10]
        
        zero_path_results.append({
            'start_position': start_pos,
            'path_count': len(complete_paths)
        })
        
        total_complete_paths += len(complete_paths)
    
    return total_complete_paths

def load_grid(filename):
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file if line.strip()]

def main():
    grid = load_grid("input.txt")
    
    result = find_complete_paths(grid)
    print(f"\nTotal complete paths: {result}")

if __name__ == "__main__":
    main()