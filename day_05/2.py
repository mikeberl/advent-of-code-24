# Counting the number of lines who are not respecting the order rules and summing up middle value of array when corrected

import os

percorso_file = os.path.join(os.getcwd(), 'input.txt')


invalid_lines = []
sum_invalid = 0

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

def correct_order(order, rules):
    valid = False
    while not valid:
        valid = True
        for i in range(len(order)):
            after_rules = [r for r in rules if r[0] == order[i]]
            before_rules = [r for r in rules if r[1] == order[i]]
            
            for r in after_rules:
                if r[1] in order and order.index(r[1]) < i:
                    idx = order.index(r[1])
                    order[i], order[idx] = order[idx], order[i]
                    valid = False
                    break
            
            for r in before_rules:
                if r[0] in order and order.index(r[0]) > i:
                    idx = order.index(r[0])
                    order[i], order[idx] = order[idx], order[i]
                    valid = False
                    break
            
            if not valid:
                break
    return order




with open(percorso_file, 'r') as file:
    lines = [line.strip() for line in file] 

# getting rules and order to test
pipe_lines = [line for line in lines if '|' in line]
comma_lines = [line for line in lines if ',' in line]
rules = [tuple(map(int, line.split('|'))) for line in pipe_lines]
number_lists = [list(map(int, line.split(','))) for line in comma_lines]

for n in number_lists:
    if (not check_rules(n, rules)):
        invalid_lines.append(n)

for n in invalid_lines:
    valid = correct_order(n, rules)
    sum_invalid += valid[int(len(n) / 2)]
print(f'Sum of the middle values of all the invalid pages sequences after correcting them is {sum_invalid}')
