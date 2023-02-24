from math import *

## Kiểm tra dữ liệu nhập vào
def check_numberic(str_input):
    a = input(str_input)
    if a.isnumeric():
        b = int(a)
        if b < 0 :
            return check_numberic(str_input)
        else:
            return b
    else:
        return check_numberic(str_input)

a = check_numberic("Nhập vào số a: ")
b = check_numberic("Nhập vào số b: ")
c = check_numberic("Nhập vào số c: ")
S = 0
S = a+b+c

print(str(a)+' + '+str(b)+' + '+str(c)+' = '+str(S))