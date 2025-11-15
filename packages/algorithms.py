from .common import *

# COMMON ALGORITHMS

# insert '0' bits to binary
def add_bits(n, binary, bits):
    while len(binary) < bits:
        # insert '0' bit to leftmost bit
        binary[:0] = ['0']
    if n < 0: binary = negative_binary(binary)
    return binary

# format binary for better visual
def format_binary(n, binary, skip_add_bits = False):
    # get needed length for displaying binary
    bit_length = max(8, ((abs(n).bit_length() + 7) // 8) * 8)
    
    # add 8 more bits when n >= 0 and the leftmost binary is '1'
    if n >= 0 and abs(n).bit_length() == bit_length:
        bit_length += 8
    
    # add_bit() is ONLY skipped when we have the finished binary (from binary to integer)
    if not skip_add_bits:
        binary = add_bits(n, binary, bit_length)
    
    if bit_length > 8:
        for i in range(8, bit_length, 9):
            binary.insert(i, ' ')
    
    return binary

# "INTEGER TO BINARY" ALGORITHMS

# convert interger |n| to binary
def interger_to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary = binary[::-1]
    return binary

# convert |n| binary to negative binary
def negative_binary(binary):
    binary[0] = '1'
    binary = one_complement(binary, len(binary) - 1)
    binary = two_complement(binary, len(binary) - 1)
    return binary

def one_complement(binary, right):
    for bit in range(right, 0, -1):
        binary[bit] = '1' if binary[bit] == '0' else '0'
    return binary

def two_complement(binary, right):
    # add 1 to the current binary
    for bit in range(right, -1, -1):
        if binary[bit] == '0':
            binary[bit] = '1'
            return binary
        binary[bit] = '0'
    return binary

# "BINARY TO INTEGER" ALGORITHMS

# get sum/result of binary
def binary_sum(binary):
    bit_index = 0
    sum = 0
    for i in binary[::-1]:
        if i == '1':
            sum += 2 ** bit_index
        bit_index += 1
    return sum

# get negative sum/result of binary
def negative_binary_result(binary):
    inverse_bit(binary, len(binary) - 1)
    one_addition(binary, len(binary) - 1)
    return -1 * binary_sum(binary)

""""
inverse all bits of binary
0 => 1
1 => 0
"""
def inverse_bit(binary, right):
    for bit in range(right, -1, -1):
        binary[bit] = '1' if binary[bit] == '0' else '0'
    return binary

# add one to binary
def one_addition(binary, right):
    for bit in range(right, -1, -1):
        if binary[bit] == '0':
            binary[bit] = '1'
            return binary
        binary[bit] = '0'
    return binary