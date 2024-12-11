from collections import Counter


def count_frequencies(array):
    frequency = Counter(array)
    
    frequency_list = list(frequency.items())
    
    return frequency_list

def check_stones(numeri):
    for _ in range(25):
        i = 0
        while i < len(numeri):
            if numeri[i] == 0:
                numeri[i] += 1
            elif len(str(abs(numeri[i]))) % 2 == 0:
                numero_str = str(numeri[i])
                meta = len(numero_str) // 2
                primo = int(numero_str[:meta])
                secondo = int(numero_str[meta:])

                numeri[i:i+1] = [primo, secondo]
                i +=1
            else:
                numeri[i] *= 2024

            i += 1
    return numeri

with open('input.txt', 'r') as file:
    numeri = list(map(int, file.read().split()))

# first assignment
result25 = check_stones(numeri)
print(len(result25))


different_numbers = count_frequencies(result25)


depth = [] # to not recalculate arrays between result50 and final result
different_numbers_50 = {}

for key, count in different_numbers:
    
    result50 = check_stones([key])
    depth.append((key, len(result50)))
    
    for num in result50:
        if num in different_numbers_50:
            different_numbers_50[num] += count
        else:
            different_numbers_50[num] = count

total_sum = 0

for key, count in different_numbers_50.items():
    if key in depth:
        total_sum += depth[key] * count
    else:
        total_sum += len(check_stones([key])) * count
print("Result:", total_sum)
