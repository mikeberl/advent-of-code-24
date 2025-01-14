# Parsing string and perform multiplication when found
# do() and don't() enable and disable the inclusion of the next multiplications

import os
import re

percorso_file = os.path.join(os.getcwd(), 'input.txt')

result = 0
mul_enabled = True
    
with open(percorso_file, 'r') as file:
    content = file.read()
    tokens = re.findall(r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))', content)

    for token in tokens:
        # check for enabled disabled
        if token == 'do()':
            mul_enabled = True
        elif token == 'don\'t()':
            mul_enabled = False
        # mul if enabed
        elif mul_enabled and token.startswith('mul('):
            x, y = re.findall(r'mul\((\d+),(\d+)\)', token)[0]
            result += int(x) * int(y)
print(f"Sum of multiplications with do and don't: {result}")
