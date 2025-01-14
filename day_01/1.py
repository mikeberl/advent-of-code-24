# Find the sum of the difference between numbers of the first and second column in ascending order

import os

percorso_file = os.path.join(os.getcwd(), 'input.txt')

first_column = []
second_column = []
sum = 0

with open(percorso_file, 'r') as file:
    for line in file:
        num1, num2 = map(int, line.strip().split())
        first_column.append(num1)
        second_column.append(num2)

first_column.sort()
second_column.sort()

for i in range(len(first_column)):
    sum += abs(first_column[i] - second_column[i])

print(f'The sum of the difference between the numbers of the first and second column in ascending order: {sum}')