# A robot with a specific keyboard is used to move another robot with a specific 
# keyboard that is used to move a robot with a specific keyboard.
# Result is the amount of clicks on the keyboard of the last robot of this chain

import re
from itertools import permutations
from collections import defaultdict

def read_codes(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def extract_numeric_part(code):
    return re.sub(r'[^0-9]', '', code)

def get_keypad():
    return {
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '0': (3, 1), 'A': (3, 2)
    }

def get_keypad_2():
    return {
        '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2)
    }

def find_shortest_path(start, target, keypad):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    reverse_dirs = {(-1, 0): '^', (1, 0): 'v', (0, -1): '<', (0, 1): '>'}

    start_pos = keypad[start]
    target_pos = keypad[target]

    vert_moves = target_pos[0] - start_pos[0]
    horz_moves = target_pos[1] - start_pos[1]

    path = ''
    if vert_moves != 0:
        path += abs(vert_moves) * reverse_dirs[(vert_moves // abs(vert_moves), 0)]
    if horz_moves != 0:
        path += abs(horz_moves) * reverse_dirs[(0, horz_moves // abs(horz_moves))]

    perm = set(''.join(p) for p in permutations(path))

    valid_perm = []
    for p in perm:
        current_pos = start_pos
        is_valid = True
        for move in p:
            if move != 'A':
                direction = directions[move]
                new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                if new_pos not in keypad.values():
                    is_valid = False
                    break
                current_pos = new_pos
        if is_valid:
            valid_perm.append(p)

    valid_perm = [p + 'A' for p in valid_perm]

    scores = [(p, calculate_mobility_score(p)) for p in valid_perm]
    min_score = min(score for _, score in scores)

    final_perm = [p for p, score in scores if score == min_score]

    return final_perm

def calculate_mobility_score(path):
    score = 0
    ch = path[0]
    for i in range(1, len(path)):
        if path[i] != ch:
            score += 1
            ch = path[i]
    return score

def get_path_for_code(code, keypad, memo):
    current_key = 'A'
    all_paths = ['']

    for digit in code:
        if (current_key, digit) in memo:
            paths_for_step = memo[(current_key, digit)]
        else:
            paths_for_step = find_shortest_path(current_key, digit, keypad)
            memo[(current_key, digit)] = paths_for_step

        new_paths = []
        for existing_path in all_paths:
            for new_path in paths_for_step:
                new_paths.append(existing_path + new_path)

        all_paths = new_paths 
        current_key = digit

    return all_paths 

def main():
    keypad = get_keypad()
    keypad2 = get_keypad_2()
    codes = read_codes('input.txt')
    result = 0
    memo = {} 
    for code in codes:
        min_len = 10000
        paths = get_path_for_code(code, keypad, memo)
        print(f"Paths for code {code}: {paths}")
        for path in paths:
            paths2 = get_path_for_code(path, keypad2, memo)
            for path2 in paths2:
                paths3 = get_path_for_code(path2, keypad2, memo)
                for path3 in paths3:
                    if len(path3) < min_len:
                        min_len = len(path3)
        print(f"Multiplying {min_len} with {extract_numeric_part(code)}")
        result += min_len * int(extract_numeric_part(code))
    print("Result: ", result)

if __name__ == "__main__":
    main()
