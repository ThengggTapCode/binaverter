from .common import *

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
    binary = one_complement(binary, len(binary) - 1)
    binary = two_complement(binary, len(binary) - 1)
    return binary

def one_complement(binary, right):
    for bit in range(right, 0, -1):
        binary[bit] = 1 if binary[bit] == 0 else 0
    return binary

def two_complement(binary, right):
    # add 1 to the current binary
    for bit in range(right, -1, -1):
        if binary[bit] == 0:
            binary[bit] = 1
            return binary
        binary[bit] = 0
    return binary
    
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
                print(Fore.YELLOW + Style.BRIGHT + "Thoát lựa chọn...\n", Style.RESET_ALL)
                return
            print_error("VUI LÒNG CHỈ NHẬP SỐ NGUYÊN")
            continue
        
        # convert |n| interger to binary
        binary = interger_to_binary(abs(n))
        
        # |n| >= 2^23 => 32-bit binary
        if abs(n) >= 2 ** 23:
            binary = add_bits(n, binary, 32)
            print_binary(n, binary, 'itb')
            
        # |n| >= 2^15 => 24-bit binary
        elif abs(n) >= 2 ** 15:
            binary = add_bits(n, binary, 24)
            print_binary(n, binary, 'itb')
            
        # |n| >= 2^7 => 16-bit binary
        elif abs(n) >= 2 ** 7:
            binary = add_bits(n, binary, 16)
            print_binary(n, binary, 'itb')
        
        # |n| < 2^7 => 8-bit binary
        else:
            binary = add_bits(n, binary, 8)
            print_binary(n, binary, 'itb')