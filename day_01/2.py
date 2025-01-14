# Find the multiplication of the difference between numbers of the first and second column in ascending order

import os

percorso_file = os.path.join(os.getcwd(), 'input.txt')

first_column = []
second_column = []
result = 0

with open(percorso_file, 'r') as file:
    for line in file:
        num1, num2 = map(int, line.strip().split())
        first_column.append(num1)
        second_column.append(num2)

result = 0

for f in first_column:
    multiplier = 0
    for s in second_column:
        if (f == s) :
            multiplier += 1
    result += multiplier * f

print(f'The similary score for the two columns is: {result}')