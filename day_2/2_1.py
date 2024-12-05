import os

percorso_file = os.path.join(os.getcwd(), 'input.txt')

valid_lines_counter = 0
lines = []


with open(percorso_file, 'r') as file:
    lines = [[int(x) for x in line.strip().split()] for line in file]

for line in lines:
    ascending = line[0] <= line[1]
    valid = True
    x = line[0]

    for i in range(1, len(line)):
        diff = abs(x - line[i])
        
        if diff < 1 or diff > 3 or (x < line[i]) != ascending:
            valid = False
            break  # Stop further checks if invalid
        
        x = line[i]
    
    if valid:
        valid_lines_counter += 1

print(f'Input file has {valid_lines_counter} valid lines out of {len(lines)}')
