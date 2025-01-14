# checking if a given number is a combinations of sum and multiplications of the following ones in reading order

def generate_combinations(numbers):
    
    def recursive_combine(current_results, next_index):
        # Stop recursion
        if next_index >= len(numbers):
            return current_results
        
        next_results = set()
        
        # first cicle
        if not current_results:
            next_results.add(numbers[0] + numbers[1])
            next_results.add(numbers[0] * numbers[1])
            return recursive_combine(next_results, 2)
        
        for curr in current_results:
            next_results.add(curr + numbers[next_index])
            next_results.add(curr * numbers[next_index])            
        
        return recursive_combine(next_results, next_index + 1)
    
    combinations = recursive_combine(set(), 0)
    return combinations

file_path = "input.txt"
result = 0

with open(file_path, "r") as file:
    for line in file:
        key, values = line.split(":")
        key = int(key.strip())
        values = list(map(int, values.strip().split()))
        
        combinations = generate_combinations(values)
        
        if key in combinations:
            result += key
        else:
            print(f"Key {key} with values {values} not valid.")

print(f"Final Result: {result}")