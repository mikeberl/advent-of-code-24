# performing operations mix /prune of numbers

input_file = "input.txt"

PRUNING_LIMIT = 16777216
ITERATIONS = 2000

def mix(secret_number, value):
    return secret_number ^ value

def prune(secret_number):
    return secret_number % PRUNING_LIMIT

with open(input_file, "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

result = 0
for secret_number in numbers:
    for _ in range(ITERATIONS):
        # Step 1: Multiply by 64, mix, and prune
        secret_number = mix(secret_number, secret_number * 64)
        secret_number = prune(secret_number)

        # Step 2: Divide by 32, round down, mix, and prune
        division_result = secret_number // 32
        secret_number = mix(secret_number, division_result)
        secret_number = prune(secret_number)

        # Step 3: Multiply by 2048, mix, and prune
        secret_number = mix(secret_number, secret_number * 2048)
        secret_number = prune(secret_number)

    # Print the final result for this secret number
    result += secret_number
    print(secret_number)

print("Result: ", result)