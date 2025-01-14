# Parsing string and perform multiplication when found

import os
import re

percorso_file = os.path.join(os.getcwd(), 'input.txt')

result = 0
    
with open(percorso_file, 'r') as file:
    content = file.read()
    #parsing
    multiplications = re.findall(r'mul\((\d+),(\d+)\)', content)
    
    # summing all multiplications
    for x, y in multiplications:
        result += int(x) * int(y)

print(f"Sum of multiplications: {result}")

