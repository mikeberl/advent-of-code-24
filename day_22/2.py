# performing operations mix /prune of numbers
# Finding the best sum of results after a certain combinations of numbers

def mix(secret_number, value):
    return secret_number ^ value

def prune(secret_number):
    return secret_number % PRUNING_LIMIT

def find_best_sum(all_iterations):
    sequence_dict = {}
    for iter in all_iterations:
        seq_in_iter = []
        for i in range(len(iter)):
            if i < 4:
                continue
            sequence = (iter[i][1], iter[i-1][1], iter[i-2][1], iter[i-3][1])
            if sequence in seq_in_iter:
                continue
            else:
                seq_in_iter.append(sequence)
            if sequence in sequence_dict:
                sequence_dict[sequence] += iter[i][0]
            else:
                sequence_dict[sequence] = iter[i][0]
    
    max_key = max(sequence_dict.items(), key=lambda x: x[1])
    print(f"Sequence with highest sum: {max_key[0]}")
    print(f"Sum: {max_key[1]}")
    
    return max_key

intermediate_results = []
for secret_number in numbers:
    previous_unit_digit = -1 
    number_iterations = []
    
    for iteration in range(ITERATIONS):
        secret_number = mix(secret_number, secret_number * 64)
        secret_number = prune(secret_number)

        division_result = secret_number // 32
        secret_number = mix(secret_number, division_result)
        secret_number = prune(secret_number)

        secret_number = mix(secret_number, secret_number * 2048)
        secret_number = prune(secret_number)

        unit_digit = secret_number % 10
        if previous_unit_digit == -1:
            difference = 0
        else:
            difference = unit_digit - previous_unit_digit

        number_iterations.append((unit_digit, difference))
        previous_unit_digit = unit_digit

    intermediate_results.append(number_iterations)


input_file = "input.txt"

PRUNING_LIMIT = 16777216
ITERATIONS = 2000

with open(input_file, "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

result = find_best_sum(intermediate_results)
sequence = result
print(f"Result (seq, sum): {sequence}")
