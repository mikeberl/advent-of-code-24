# Counting the number of lines who are respecting the order rules and summing up their middle

import os

percorso_file = os.path.join(os.getcwd(), 'input.txt')

result = 0

def check_rules(order, rules):
    for i in range(len(order)):
        after_rules = [r for r in rules if r[0] == order[i]]
        before_rules = [r for r in rules if r[1] == order[i]]
        
        for r in after_rules:
            if r[1] in order and order.index(r[1]) < i:
                return False
        for r in before_rules:
            if r[0] in order and order.index(r[0]) > i:
                return False
    return True



with open(percorso_file, 'r') as file:
    lines = [line.strip() for line in file] 

# getting rules and order to test
pipe_lines = [line for line in lines if '|' in line]
comma_lines = [line for line in lines if ',' in line]
rules = [tuple(map(int, line.split('|'))) for line in pipe_lines]
number_lists = [list(map(int, line.split(','))) for line in comma_lines]

for n in number_lists:
    if (check_rules(n, rules)):
        result += n[int(len(n) / 2)]

print(f'Sum of the middle values of all the valid pages sequences is {result}')

