from .common import *
from .algorithms import *

def ttb_menu():
    while True:
        text = input("Nhập văn bản cần chuyển đổi (nhập một kí tự 'T' để thoát):\n")

        # exit the current choice
        if text.lower() == 't':
            clear_terminal()
            print(Fore.YELLOW + Style.BRIGHT + "Đã thoát lựa chọn!\n" + Style.RESET_ALL)
            return
        
        binary = []
        index = 0
        
        for i in text:
            # get ascii value of the current character
            ascii_value = ord(i)
            
            # convert ascii value to binary
            binary_value = interger_to_binary(ascii_value)
            
            # format the binary of ascii value
            binary_value = format_binary(ascii_value, binary_value, False, True)
            binary_value = ''.join(binary_value)
            
            # add the sub-binary to the binar
            binary.append(binary_value)
            
            # spaces is added ONLY when text is more thanb 1 character and index is lesser than last index of text
            if len(text) > 1 and index < len(text) - 1:
                binary.append(' ')
        
        clear_terminal()
        # print the final result
        print_binary(None, binary, 'ttb', text)