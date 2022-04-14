"""
Số mạnh mẽ là số khi chia hết cho số nguyên tó thì cũng chia hết cho cả bình phương của số nguyên tố đó
Ví dụ: 25 là soos mạnh mẽ, vì nó chia hết cho số nguyên tố 5 và chia hết cho cả bình phương của của 5 là 25
Viết chương trình kiệt kê các số mạnh mẽ không vượt quá 1000
"""

from math import *

def nguyento(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(sqrt(x)) + 1):
        if a % i == 0:
            return False
    return True

s = ''
a = 2
while a < 1000:
    for i in range (2, a):
        if a % i == a % (i*i) == 0:
            if nguyento(i):
                s += str(a) + ' '
                break
    a += 1

print(s)