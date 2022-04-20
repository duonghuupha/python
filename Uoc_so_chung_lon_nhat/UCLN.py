"""
Nhập vào 3 số từ bàn phím, kiểm soát dữ liệ nhập vào là số nguyên dương.
Lập trình tìm ước chung lớn nhất của 3 số trên.
Ví dụ: Nhập vào 3 số: 4, 6, 12 thì kết quả ước chung lớn nhất là 2
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

day_so = [a, b, c]
day_so.sort()
uocso = []
for i in range(1, day_so[0] + 1):
    if day_so[0] % i == 0 and day_so[1] % i == 0 and day_so[2] % i == 0:
        uocso.append(i)

uocso.sort()
print(uocso[-1])