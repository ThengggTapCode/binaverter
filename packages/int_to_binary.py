def print_binary(n, binary):
    print(f'{n} = ', end='')
    for i in binary:
        print(i,end='')
    print()

def interger_to_binary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n //= 2
    binary = binary[::-1]
    return binary

def add_bits(n, binary, bits):
    while len(binary) < bits:
        binary[:0] = [0]
    if n < 0: binary = negative_binary(binary)
    return binary

def negative_binary(binary):
    binary[0] = 1
    print(binary)
    binary = one_complement(binary, 0, len(binary))
    print(binary)
    binary = two_complement(binary, 0, len(binary))
    print(binary)
    return binary

def one_complement(binary, left, right):
    for i in range(left + 1, right):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0
    return binary

def two_complement(binary, left, right):
    for i in range(right - 1, left, -1):
        if binary[i] == 0:
            binary[i] = 1
            return binary
        binary[i] = 0
    
def itb_menu():
    try:
        n = int(input("Nhập số nguyên n: "))
    except ValueError:
        print("Vui lòng nhập n là số nguyên!")
        return
    
    binary = interger_to_binary(abs(n))
    print(binary)
    
    if abs(n) >= 2 ** 23:
        binary = add_bits(n, binary, 32)
        
        binary.insert(8, ' ')
        binary.insert(17, ' ')
        binary.insert(26, ' ')
        print_binary(n, binary)
        
    elif abs(n) >= 2 ** 15:
        binary = add_bits(n, binary, 24)
        
        binary.insert(8, ' ')
        binary.insert(17, ' ')
        print_binary(n, binary)
    
    elif abs(n) >= 2 ** 7:
        binary = add_bits(n, binary, 16)
        
        binary.insert(8, ' ')
        print_binary(n, binary)

    else:
        binary = add_bits(n, binary, 8)
        print_binary(n, binary)