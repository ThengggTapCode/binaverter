from .common import *

# get sign of binary
def get_binary_sign():
    while True:
        sign = input("Nhập dấu của mã nhị phân (+, -): ")
        if sign != '+' and sign != '-':
            print_error("DẤU ĐÃ NHẬP KHÔNG HỢP LỆ!")
        else:
            return sign

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

# binary to interger menu
def bti_menu():
    while True:
        # get string input
        binary_temp = input("Nhập mã nhị phân (nhập 'T' để thoát): ").lower().replace(' ', '')
        # string input is converted to list
        binary = list(binary_temp)
        is_binary = True
        
        # exit the current choice
        if len(binary) == 1 and 't' in binary:
            clear_terminal()
            print(Fore.YELLOW + Style.BRIGHT + "Thoát lựa chọn...\n", Style.RESET_ALL)
            return
        
        # check for invalid binary
        for bit in range(0, len(binary)):
            if binary[bit] != '0' and binary[bit] != '1':
                is_binary = False
                break
        
        if not is_binary:
            clear_terminal()
            print_error("MÃ NHỊ PHÂN ĐÃ NHẬP KHÔNG HỢP LỆ!")
            continue
        
        # get sign of binary
        sign = get_binary_sign()
        
        # check binary sign to calculate and solve the binary
        if sign == '+':
            sum = binary_sum(binary)
        elif sign == '-':
            sum = negative_binary_result(binary)
        
        # print the binary
        print_binary(sum, binary_temp, 'bti')
