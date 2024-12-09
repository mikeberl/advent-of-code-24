
with open("input.txt", "r") as file:
    numero = file.read()

memory = []
for index, cifra in enumerate(numero):
    if index % 2 == 0:  # even
        for l in range(int(cifra)):
            memory.append(int(index / 2))
    else:  # odd
        for l in range(int(cifra)):
            memory.append('.')
# print(memory)

analyzed_number = [] # to avoid check multiple times for the same block
for index, number in enumerate(reversed(memory)):
    if number == '.':
        continue
    elif number in analyzed_number:
        continue
    elif number == 0:
        break
    else:
        act_nr = number
        analyzed_number.append(act_nr)
        count = 0
        while(memory[-1 - index - count] == act_nr):
            count += 1
        for i in range(len(memory)):
            if memory[i] == act_nr:
                break
            if memory[i] != '.':
                continue
            else:
                count2 = 0
                while i + count2 < len(memory) and memory[i + count2] == '.':
                    count2 += 1
                if (count2 >= count):
                    # print(f'Block {act_nr} has place between index {i} and {i + count2}')
                    for x in range(count):
                        memory[i + x] = act_nr
                        memory[-1 - index- x] = '.'
                    break

print("Memory after replacements:", memory)
result = 0
for index, number in enumerate(memory):
     if (number != '.'):
        result += index * number
print("Result: ", result)
    