# Given a list of keys and locks
# How many unique lock/key pairs fit together without overlapping in any column?

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    blocks = [block.splitlines() for block in content.strip().split('\n\n')]
    return blocks

def convert_to_heights(block):
    num_columns = len(block[0])
    heights = []

    for col in range(num_columns):
        height = 0
        for row in range(len(block)):
            if block[row][col] == '#':
                height = len(block) - row
                break
        heights.append(height)

    return heights

def convert_to_key(block):
    num_columns = len(block[0])
    heights = []

    for col in range(num_columns):
        height = 0
        for row in range(len(block)):
            if block[row][col] == '#':
                height = len(block) - row - 1
                break
        heights.append(height)

    return heights

def is_key_fitting(lock, key):
    for lock_height, key_height in zip(lock, key):
        if lock_height + key_height > len(lock):
            return False
    return True

def main():
    filename = 'input.txt'
    blocks = read_file(filename)

    locks = []
    keys = []

    for block in blocks:
        if block[0] == '#####':
            locks.append(convert_to_key(list(reversed(block))))
        elif block[-1] == '#####':
            keys.append(convert_to_key(block))

    print("Locks (as heights):")
    for i, lock in enumerate(locks):
        print(f"Lock {i}: {lock}")

    print("\nKeys (as heights):")
    for i, key in enumerate(keys):
        print(f"Key {i}: {key}")

    result = 0
    print("\nKey-Lock Compatibility:")
    for lock_idx, lock in enumerate(locks):
        for key_idx, key in enumerate(keys):
            if is_key_fitting(lock, key):
                print(f"Lock {lock_idx} fits with Key {key_idx}")
                result += 1
            else:
                print(f"Lock {lock_idx} does NOT fit with Key {key_idx}")
    print("Result: ", result)
if __name__ == '__main__':
    main()
