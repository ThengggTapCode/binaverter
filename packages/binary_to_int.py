from .common import *

def get_int_sign():
    while True:
        sign = input("Nhập dấu của số nguyên (+, -): ")
        clear_terminal()
        if sign != '+' and sign != '-':
            print_error("DẤU ĐÃ NHẬP KHÔNG HỢP LỆ!")
        return sign

def binary_sum(binary, end):
    bit = 0
    sum = 0
    for i in range(end - 1, 0, -1):
        if binary[i] == '+':
            sum += 2 ** bit
        bit += 1
    
    return sum
        
def bin_to_int():
    while True:
        binary = list(input("Nhập mã nhị phân: "))
        is_binary = True
        
        for bit in binary:
            if bit == ' ':
                binary.remove(bit)
            if bit != '0' and binary != '1':
                is_binary = False
                break
        
        if not is_binary:
            clear_terminal()
            print_error("MÃ NHỊ PHÂN ĐÃ NHẬP KHÔNG HỢP LỆ!")
            continue
        
        bits = len(binary)
        
        sign = get_int_sign()
        if sign == "+":
            sum = binary_sum(binary)
