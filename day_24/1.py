# performing bit-wise operations between registers
# Result is the decimal number obtained by converting the binary number
# obtained by listing all the z-Register (z1,z2,z3,..)  after all the operations are completed

import re

def parse_registers_and_operations(file_path):

    registers = {}
    operations = []

    with open(file_path, 'r') as file:
        content = file.read()
        sections = content.split('\n\n')

        for line in sections[0].splitlines():
            match = re.match(r"(\w+):\s*(\d+)", line)
            if match:
                register, value = match.groups()
                registers[register] = int(value)

        for line in sections[1].splitlines():
            match = re.match(r"(\w+)\s+(AND|OR|XOR)\s+(\w+)\s*->\s*(\w+)", line)
            if match:
                op1, operation, op2, result = match.groups()
                operations.append((op1, operation, op2, result))

    return registers, operations

def execute_operations(registers, operations):
    pending_operations = operations.copy()
    completed_z_registers = set()

    while pending_operations:
        next_operations = []
        for op1, operation, op2, result in pending_operations:
            if op1 in registers and op2 in registers:
                val1 = registers[op1]
                val2 = registers[op2]

                if operation == "AND":
                    registers[result] = val1 & val2
                elif operation == "OR":
                    registers[result] = val1 | val2
                elif operation == "XOR":
                    registers[result] = val1 ^ val2

                if result.startswith('z'):
                    completed_z_registers.add(result)
            else:
                next_operations.append((op1, operation, op2, result))

        pending_operations = next_operations

def process_register_sum(registers, letter):
    z_registers = {key: value for key, value in registers.items() if key.startswith(letter)}
    binary_number = ''.join(str(z_registers[key]) for key in reversed(sorted(z_registers)))

    decimal_number = int(binary_number, 2)
    print(f"Binary number formed: {binary_number}")
    print(f"Decimal equivalent: {decimal_number}")

    return binary_number, decimal_number

def main():
    file_path = "input.txt"
    registers, operations = parse_registers_and_operations(file_path)

    execute_operations(registers, operations)

    z_bin, z_dec = process_register_sum(registers, 'z')
    y_bin, y_dec = process_register_sum(registers, 'y')
    x_bin, x_dec = process_register_sum(registers, 'x')

if __name__ == "__main__":
    main()
