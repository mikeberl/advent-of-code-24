
with open("input.txt", "r") as file:
    numero = file.read()

initial_memory = []
for index, cifra in enumerate(numero):
    if index % 2 == 0: #even
        for l in range(int(cifra)):
            initial_memory.append(int(index / 2))
    else:  # odd
        for l in range(int(cifra)):
            initial_memory.append('.')
# print(starting_array)

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