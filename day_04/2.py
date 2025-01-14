# Find CROSSED occurrences of XMAS in a matrix (8 directions)

word = ['X', 'M', 'A', 'S']

def find_sequence(matrix):
    lines = len(matrix)
    columns = len(matrix[0])

    occurence = 0

    for line in range(lines):
        for letter in range(columns):
            # To avoid out of index
            if (line + 1 < lines and 
                line + -1 >= 0 and 
                letter + 1 < columns and 
                letter + -1 >= 0):
                
                if (matrix[line][letter] == 'A'):
                    if (matrix[line - 1][letter - 1] == 'M' and
                        matrix[line - 1][letter + 1] == 'M' and
                        matrix[line + 1][letter - 1] == 'S' and
                        matrix[line + 1][letter + 1] == 'S'):
                        occurence += 1
                    elif (matrix[line - 1][letter - 1] == 'S' and
                        matrix[line - 1][letter + 1] == 'S' and
                        matrix[line + 1][letter - 1] == 'M' and
                        matrix[line + 1][letter + 1] == 'M'):
                        occurence += 1
                    elif (matrix[line - 1][letter - 1] == 'S' and
                        matrix[line - 1][letter + 1] == 'M' and
                        matrix[line + 1][letter - 1] == 'S' and
                        matrix[line + 1][letter + 1] == 'M'):
                        occurence += 1
                    elif (matrix[line - 1][letter - 1] == 'M' and
                        matrix[line - 1][letter + 1] == 'S' and
                        matrix[line + 1][letter - 1] == 'M' and
                        matrix[line + 1][letter + 1] == 'S'):
                        occurence += 1
                
    return occurence


with open('input.txt', 'r') as file:
    input_text = file.read()
matrix = [list(line) for line in input_text.splitlines()]

occurrences = find_sequence(matrix)
print(f'The CROSSED word XMAS was found {find_sequence(matrix)} times')