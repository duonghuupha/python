"""
Với một số nguyên dương bất kỳ, thay thế số đó bằng tổng bình phương các chữ số của nó và cứ lặp lại
quá trình đó sẽ có những trường hợp sau xảy ra:
Kết thúc bằng 1 - Là số hạnh phúc
Kêt thúc bằng 0 - Là số buồn bã
Lặp vô hạn lần - Số đó không hạn phúc cũng không buồn bã
VD: Số 44
- lần 1:  4^2 + 4^2 = 16 + 16 = 32
- lần 2: 3^2 + 2^2 = 9 + 4 = 13
- lần 3: 1^2 + 3^2 = 1 + 9 = 10
- lần 4: 1^2 + 0^2 = 1
Vậy số 44 là số hạnh phúc
Hãy viết chương trình kiểm tra xem ngày sinh của một người nào đó có phải là số hanh phúc không?
"""
from math import *

a = input("Nhập ngày sinh của bạn: ")

def so_hanh_phuc(x):
    list = []
    list[:0] = x
    b = 0
    for item in list:
        c = int(item)
        b += c**2
    if b == 1:
        return True
    elif b == 0:
        return False
    else:
        hanh_phuc = str(b)
        return so_hanh_phuc(hanh_phuc)

"""
if a == 1:
    print("Số " + a + " là số hạnh phúc")
else:
    print(so_hanh_phuc(a))
"""
if so_hanh_phuc(a):
    print ("Số " + a + ' là số hạnh phúc')
else:
    print ("Số " + b + ' là số buồn bã')