from .common import *

# print final binary result
def print_binary(n, binary):
    print(Fore.GREEN + f'{n} = ', end='')
    for i in binary:
        print(i,end='')
    print(Fore.RESET + "\n")

# convert interger |n| to binary
def interger_to_binary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n //= 2
    binary = binary[::-1]
    return binary

# insert '0' bits to binary
def add_bits(n, binary, bits):
    while len(binary) < bits:
        # insert '0' bit to leftmost bit
        binary[:0] = [0]
    if n < 0: binary = negative_binary(binary)
    return binary

# convert |n| binary to negative binary
def negative_binary(binary):
    binary[0] = 1
    binary = one_complement(binary, 0, len(binary))
    binary = two_complement(binary, 0, len(binary))
    return binary

def one_complement(binary, left, right):
    for i in range(left + 1, right):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0
    return binary

def two_complement(binary, left, right):
    # add 1 to the current binary
    for i in range(right - 1, left, -1):
        if binary[i] == 0:
            binary[i] = 1
            return binary
        binary[i] = 0
    
def itb_menu():
    while True:
        try:
            # get interger n
            n = input("Nhập số nguyên (nhập T để thoát lựa chọn): ")
            clear_terminal()
            n = int(n)
        
        # ValueError exception
        except ValueError:
            if n.lower() == 't':
                print(Fore.YELLOW + Style.BRIGHT + "\nThoát lựa chọn...", Style.RESET_ALL)
                return
            print_error("VUI LÒNG CHỈ NHẬP SỐ NGUYÊN")
            continue
        
        # convert |n| interger to binary
        binary = interger_to_binary(abs(n))
        
        # |n| >= 2^23 => 32-bit binary
        if abs(n) >= 2 ** 23:
            binary = add_bits(n, binary, 32)
            
            binary.insert(8, ' ')
            binary.insert(17, ' ')
            binary.insert(26, ' ')
            print_binary(n, binary)
            
        # |n| >= 2^15 => 24-bit binary
        elif abs(n) >= 2 ** 15:
            binary = add_bits(n, binary, 24)
            
            binary.insert(8, ' ')
            binary.insert(17, ' ')
            print_binary(n, binary)
            
        # |n| >= 2^7 => 16-bit binary
        elif abs(n) >= 2 ** 7:
            binary = add_bits(n, binary, 16)
            
            binary.insert(8, ' ')
            print_binary(n, binary)
        
        # |n| < 2^7 => 8-bit binary
        else:
            binary = add_bits(n, binary, 8)
            print_binary(n, binary)