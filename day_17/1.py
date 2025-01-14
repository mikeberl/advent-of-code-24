# performing operations with a 3-bit computer with specific operations setup

def adv(registers, operand):
    if operand < 4:
        registers['A'] = registers['A'] // (2 ** operand)
    elif operand == 4:
        registers['A'] = registers['A'] // (2 ** registers['A'])
    elif operand == 5:
        registers['A'] = registers['A'] // (2 ** registers['B'])
    elif operand == 6:
        registers['A'] = registers['A'] // (2 ** registers['C'])
    return registers

def bxl(registers, operand):
    registers['B'] = registers['B'] ^ operand
    return registers

def bst(registers, operand):
    """Set B to operand % 8 (lowest 3 bits)"""
    if operand < 4:
        registers['B'] = operand % 8
    elif operand == 4:
        registers['B'] = registers['A'] % 8
    elif operand == 5:
        registers['B'] = registers['B'] % 8
    elif operand == 6:
        registers['B'] = registers['C'] % 8
    return registers

def jnz(registers, operand):
    return operand if registers['A'] != 0 else None

def bxc(registers, operand):
    registers['B'] = registers['B'] ^ registers['C']
    return registers

def out(registers, operand):
    if operand < 4:
        return operand % 8
    elif operand == 4:
        return registers['A'] % 8
    elif operand == 5:
        return registers['B'] % 8
    elif operand == 6:
        return registers['C'] % 8
    return 0

def bdv(registers, operand):
    if operand < 4:
        registers['B'] = registers['A'] // (2 ** operand)
    elif operand == 4:
        registers['B'] = registers['A'] // (2 ** registers['A'])
    elif operand == 5:
        registers['B'] = registers['A'] // (2 ** registers['B'])
    elif operand == 6:
        registers['B'] = registers['A'] // (2 ** registers['C'])
    return registers

def cdv(registers, operand):
    if operand < 4:
        registers['C'] = registers['A'] // (2 ** operand)
    elif operand == 4:
        registers['C'] = registers['A'] // (2 ** registers['A'])
    elif operand == 5:
        registers['C'] = registers['A'] // (2 ** registers['B'])
    elif operand == 6:
        registers['C'] = registers['A'] // (2 ** registers['C'])
    return registers

def execute_program(initial_a, initial_b, initial_c, program):
    registers = {
        'A': initial_a,
        'B': initial_b,
        'C': initial_c
    }
    
    instructions = {
        0: adv,   
        1: bxl,   
        2: bst,   
        3: jnz,   
        4: bxc,   
        5: out,   
        6: bdv,   
        7: cdv    
    }
    
    output = []
    ip = 0
    
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else 0

        jump_target = None
        if opcode == 3:
            jump_target = jnz(registers, operand)
            if jump_target is not None:
                ip = jump_target
                continue
        elif opcode == 5:
            output_val = out(registers, operand)
            output.append(output_val)
        elif opcode == 0:
            adv(registers, operand)
        elif opcode == 1:
            bxl(registers, operand)
        elif opcode == 2:
            bst(registers, operand)
        elif opcode == 4:
            bxc(registers, operand)
        elif opcode == 6:
            bdv(registers, operand)
        elif opcode == 7:
            cdv(registers, operand)
        ip += 2
        
        if ip >= len(program):
            break
    
    return registers, output

# Test cases
test_cases = [
    (44374556, 0, 0, [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 1, 5, 5, 3, 0]),
]

for a, b, c, program in test_cases:
    print(f"\nRunning program with A={a}, B={b}, C={c}")
    final_registers, output = execute_program(a, b, c, program)
    print("Output:", ",".join(map(str, output)))