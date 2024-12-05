import os

percorso_file = os.path.join(os.getcwd(), 'input.txt')

valid_lines_counter = 0

# Logic of part 1
def is_valid_sequence(sequence):
    crescente = sequence[0] < sequence[1]
    for i in range(1, len(sequence)):
        diff = abs(sequence[i-1] - sequence[i])

        if diff < 1 or diff > 3:
            return False
        if (sequence[i-1] < sequence[i]) != crescente:
            return False
    return True


# part 2
with open(percorso_file, 'r') as file:
    lines = [[int(x) for x in line.strip().split()] for line in file]

for line in lines:
    if is_valid_sequence(line):
        valid_lines_counter += 1
        continue
    else:
        for i in range(len(line)):
            shorter_line = line.copy()
            shorter_line.pop(i)
            if is_valid_sequence(shorter_line):
                valid_lines_counter += 1
                break

print(f'In the case of one number tollerance input file has {valid_lines_counter} valid lines out of {len(lines)}')
