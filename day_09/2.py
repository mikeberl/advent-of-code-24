# Defragmentation of a memory
# New rules

with open("input.txt", "r") as file:
    big_number = file.read()

memory = []
for index, figure in enumerate(big_number):
    if index % 2 == 0:  # even
        for l in range(int(figure)):
            memory.append(int(index / 2))
    else:  # odd
        for l in range(int(figure)):
            memory.append('.')

analyzed_number = [] # to avoid check multiple times for the same block
for index, figure in enumerate(reversed(memory)):
    if figure == '.':
        continue
    elif figure in analyzed_number:
        continue
    elif figure == 0:
        break
    else:
        act_nr = figure
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
                    for x in range(count):
                        memory[i + x] = act_nr
                        memory[-1 - index- x] = '.'
                    break

print("Memory after replacements:", memory)
result = 0
for index, figure in enumerate(memory):
     if (figure != '.'):
        result += index * figure
print("Result: ", result)
    