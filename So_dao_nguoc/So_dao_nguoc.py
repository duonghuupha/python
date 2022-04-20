"""
Tìm số  đảo ngược Y của một số X, biết Y gồm các chữ số của X và viết theo thứ tự ngược lại. Xuất ra kết quả là số Y mod 19
Ví dụ: 123 => 321 => 321 mod 19 = 17
"""

from math import *

def check_numberic(str_input):
    a = input(str_input)
    if a.isnumeric():
        b = int(a)
        if b < 10:
            return check_numberic(str_input)
        else:
            return b
    else:
        return check_numberic(str_input)

def listtoString(s):
    string = ""
    return (string.join(s))

a = check_numberic("Nhập vào một số lớn hơn 10: ")
a = str(a)
du_lieu = list(reversed(a))
dao_nguoc = listtoString(du_lieu)
dao_nguoc = int(dao_nguoc)
print(dao_nguoc % 19)
