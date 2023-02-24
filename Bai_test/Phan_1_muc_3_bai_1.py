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

a = check_numberic("Nhaập só nguyên dương A: ")
i = 1
while(i <= a):
    print(i)
    i += 2