"""
Số hoàn hảo là một s ố tự nhiên m à tổng tất car các ước tự nhiên thực sự của nó bằng chính nó. Trong đó
ước thực sự của một số là các ước không bằng số đó.
Viết chương trình nhập và một số tự nhiên có hai chữ số bất kỳ. In ra màn hình thông báo số vừa nhập có phải
là số hoàn hảo hay không, nếu là số hoàn hảo thì in ra tất cả cá ước của số đó
"""

from math import *

a = input("Nhập vào số nguyên có 2 chữ số: ")
a = int(a)

def listtoString(s):
    string = ""
    return (string.join(s))

s =[]
tong = 0
for i in range (1, a):
    if a % i == 0:
        tong += i
        s.append(i)
if tong == a:
    print(str(a) + " là số hoàn hảo. Các ước của " + str(a) + " là: " + listtoString(s))
else:
    print(str(a) + " không phải là số hoàn hảo")