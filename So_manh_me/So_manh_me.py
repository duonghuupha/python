"""
Số mạnh mẽ là số khi chia hết cho số nguyên tố thì cũng chia hết cho cả bình phương của số nguyên tố đó
Ví dụ: 25 là soos mạnh mẽ, vì nó chia hết cho số nguyên tố 5 và chia hết cho cả bình phương của của 5 là 25
Viết chương trình liệt kê các số mạnh mẽ không vượt quá 1000
"""

from math import *

def nguyento(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
"""
s = ''
a = 2
while a < 1000: ## Liệt kê các số từ 2 đến 1000
    for i in range (2, a):  ## liệt kê các số từ 2 đén a
        if a % i == 0 and a % (i*i) == 0: ## Nếu a  chia hết cho i và a chia hết bình phương của i
            if nguyento(i): # nếu số a thỏa điều kiện thì kiểm tra xem i có phải là số nguyên tố không
                s += str(a) + ' ' # nếu đúng thì cộng vào chuỗi
                break # và dừng vòng lặp for
    a += 1 # sau mỗi lần lặp thì thì cộng thêm 1

print(s)
"""
s = ''
a = 2
b = []
while a < 1000:
    for i in range(2, a):
        if(nguyento(i)):
            if a % i == 0 and a % i**2 == 0:
                b.append(str(i)+'-'+str(i*i)+'-'+str(a%i)+'-'+str(a%(i*i))+' '+str(a))
                s += str(a) + ' '
    a += 1
    """
    if a == 10:
        print(a)
        print(b)
        break
    """
print(s)