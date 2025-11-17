from .common import *
from .algorithms import *

# get sign of binary
def get_binary_sign():
    while True:
        sign = input("Nhập dấu của mã nhị phân (+, -): ")
        if sign != '+' and sign != '-':
            print_error("DẤU ĐÃ NHẬP KHÔNG HỢP LỆ!")
        else:
            return sign

# binary to interger menu
def bti_menu():
    while True:
        # get string input
        binary_temp = input("Nhập mã nhị phân (nhập 'T' để thoát): ").lower().replace(' ', '')
        blank_binary = False if len(binary_temp) != 0 else True

        if not blank_binary:

            # str binary is converted to list type
            binary = list(binary_temp)
            is_binary = True

            # exit the current choice
            if len(binary) == 1 and 't' in binary:
                clear_terminal()
                print(Fore.YELLOW + Style.BRIGHT + "Đã thoát lựa chọn!\n", Style.RESET_ALL)
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
            
            binary_temp = format_binary(sum, list(binary_temp), True)

            clear_terminal()
            print_binary(sum, binary_temp, 'bti')

        # sum = 0 when binwry is blank
        else:
            print_binary(0, '00000000', 'bti')
