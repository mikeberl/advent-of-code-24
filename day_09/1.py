# Defragmentation of a memory

with open("input.txt", "r") as file:
    big_number = file.read()

initial_memory = []
for index, figure in enumerate(big_number):
    if index % 2 == 0: #even
        for l in range(int(figure)):
            initial_memory.append(int(index / 2))
    else:  # odd
        for l in range(int(figure)):
            initial_memory.append('.')

final_array = []
for element in initial_memory:
    if element == '.':
        while(initial_memory[-1] == '.'):
            initial_memory.pop(-1)
        final_array.append(initial_memory.pop(-1))
    else:
        final_array.append(element)

print("Final array without free spaces:", final_array)

result = 0
for index, number in enumerate(final_array):
     result += index * number
print("Result: ", result)