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

a = check_numberic("Nhập số nguyên dương A: ")
if a % 3 == 0 or a % 5 == 0:
    print(str(a) + ' là bội số của 3 hoặc 5')
else:
    print(str(a) + ' không là bội số của 3 hoặc 5')