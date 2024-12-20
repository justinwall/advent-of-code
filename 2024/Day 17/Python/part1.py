from re import findall
from math import pow

# opcode 0
def adv(operand):
    global a, b, c

    if operand in range(4):
        a = int(a // pow(2, operand))
    elif operand == 4:
        a = int(a // pow(2, a))
    elif operand == 5:
        a = int(a // pow(2, b))
    elif operand == 6:
        a = int(a // pow(2, c))
    elif operand == 7:
        raise ValueError("Combo operand 7 is reserved!")

# opcode 1
def bxl(operand):
    global b

    b = b ^ operand

# opcode 2
def bst(operand):
    global a, b, c

    if operand in range(4):
        b = operand % 8
    elif operand == 4:
        b = a % 8
    elif operand == 5:
        b = b % 8
    elif operand == 6:
        b = c % 8
    elif operand == 7:
        raise ValueError("Combo operand 7 is reserved!")

# opcode 3
def jnz(operand):
    global i_ptr, a

    # jump to pointer - 2 to balance out the normal +2
    if a != 0:
        i_ptr = operand - 2

# opcode 4
def bxc(operand):
    global b, c

    b = b ^ c

# opcode 5
def out(operand):
    global a, b, c

    if operand in range(4):
        return str(operand % 8)
    elif operand == 4:
        return str(a % 8)
    elif operand == 5:
        return str(b % 8)
    elif operand == 6:
        return str(c % 8)
    elif operand == 7:
        raise ValueError("Combo operand 7 is reserved!")

# opcode 6
def bdv(operand):
    global a, b, c

    if operand in range(4):
        b = int(a // pow(2, operand))
    elif operand == 4:
        b = int(a // pow(2, a))
    elif operand == 5:
        b = int(a // pow(2, b))
    elif operand == 6:
        b = int(a // pow(2, c))
    elif operand == 7:
        raise ValueError("Combo operand 7 is reserved!")

# opcode 7
def cdv(operand):
    global a, b, c

    if operand in range(4):
        c = int(a // pow(2, operand))
    elif operand == 4:
        c = int(a // pow(2, a))
    elif operand == 5:
        c = int(a // pow(2, b))
    elif operand == 6:
        c = int(a // pow(2, c))
    elif operand == 7:
        raise ValueError("Combo operand 7 is reserved!")

# read input_data from file
with open("../input.txt", "r") as file:
    input_data = file.read().strip().split('\n\n')

# parse input_data for registers and program list
a, b, c = map(int, findall(r"\d+", input_data[0]))
program = list(map(int, findall(r"\d", input_data[1])))
program_size = len(program)

# run program and collect output
output = []
i_ptr = 0
while i_ptr < program_size:
    opcode, operand = program[i_ptr:i_ptr + 2]

    if opcode == 0:
        adv(operand)
    elif opcode == 1:
        bxl(operand)
    elif opcode == 2:
        bst(operand)
    elif opcode == 3:
        jnz(operand)
    elif opcode == 4:
        bxc(operand)
    elif opcode == 5:
        output += out(operand)
    elif opcode == 6:
        bdv(operand)
    elif opcode == 7:
        cdv(operand)

    i_ptr += 2

print(",".join(output))