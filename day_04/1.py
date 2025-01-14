# Find occurrences of XMAS in a matrix (8 directions)

word = ['X', 'M', 'A', 'S']

def find_sequence(matrix):
    lines = len(matrix)
    columns = len(matrix[0])
    directions = [ 
        [0, 1],     # right
        [0, -1],    # left
        [1, 0],     # down
        [-1, 0],    # up
        [1, 1],     # dia-down-right
        [1, -1],    # dia-down-left
        [-1, 1],    # dia-up-right
        [-1, -1]    # dia-up-left
    ]
    occurence = 0

    for d in directions:
        for line in range(lines):
            for letter in range(columns):
                # check to avoid out of index
                if (line + 3 * d[0] < lines and 
                    line + 3 * d[0] >= 0 and 
                    letter + 3 * d[1] < columns and 
                    letter + 3 * d[1] >= 0):
                    
                    if (matrix[line][letter] == word[0] and 
                        matrix[line + 1 * d[0]][letter + 1 * d[1]] == word[1] and
                        matrix[line + 2 * d[0]][letter + 2 * d[1]] == word[2] and
                        matrix[line + 3 * d[0]][letter + 3 * d[1]] == word[3]):
                        occurence += 1
                
    return occurence

with open('input.txt', 'r') as file:
    input_text = file.read()
matrix = [list(line) for line in input_text.splitlines()]

occurrences = find_sequence(matrix)
print(f"Occorrenze trovate: {occurrences}")
