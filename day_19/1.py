# Given a list of designs and of combinations of towels to compose the design
# find how many designs in the input file are possible to compose

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    colors = [s.strip() for s in lines[0].split(',')]
    towels = [line.strip() for line in lines[1:] if line.strip()]
    
    return colors, towels

def can_compose_string(towel, colors):
    n = len(towel)
    check = [False] * (n + 1)
    check[0] = True
    
    for i in range(1, n + 1):
        for partial in colors:
            if check[i - len(partial)] and towel[i - len(partial):i] == partial:
                check[i] = True
                break
    
    return check[n]

colors, towels = read_file('input.txt')
valid_towels = []

for i, string in enumerate(towels, start=1):
    if can_compose_string(string, colors):
        valid_towels.append((i, string))

print(f"Valid towels: {len(valid_towels)}")

