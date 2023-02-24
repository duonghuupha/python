"""
Giải biểu thức theo yêu cầu
"""
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
tu_so = 0
mau_so = 0
## Tinh tu so
tu_so = (-1)*b + (sqrt(b**2 - (4*a*c)))
## tinh mau so
mau_so = 2*a

S = tu_so/mau_so
print(S)