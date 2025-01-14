# Given a list of designs and of combinations of towels to compose the design
# find how many designs in the input file are possible to compose
# PART 2: Find in HOW MANY DIFFERENT WAYS is possible to compose the designs usings the different towels

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    colors = [s.strip() for s in lines[0].split(',')]
    towels = [line.strip() for line in lines[1:] if line.strip()]
    
    return colors, towels

def count_compositions(towel, colors):
    n = len(towel)
    check = [0] * (n + 1)
    check[0] = 1
    
    for i in range(1, n + 1):
        for partial in colors:
            if i >= len(partial) and towel[i - len(partial):i] == partial:
                check[i] += check[i - len(partial)]
    
    return check[n]

colors, towels = read_file('input.txt')
total_compositions = 0
valid_towels = []

for i, string in enumerate(towels, start=1):
    ways = count_compositions(string, colors)
    if ways > 0:
        valid_towels.append((i, string, ways))
        total_compositions += ways

print(f"Result: {total_compositions}")

