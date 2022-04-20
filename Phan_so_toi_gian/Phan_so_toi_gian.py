"""
Một chuỗi được gọi là có dạng phân số nêu snos có dạng như sau: 'Tử_số/Mẫu _số'
Viết chương trình nhập vào cuỗi có dạng phân số, sau đó xuất ra dạng tối giản của
phân số đó.
Ví dụ: Chuỗi 12/5 biểu diễn cho phân số. Dạng tối giản của phân số là 12/5
    Chuỗi 12/8 biểu diễn cho phân số. Dạng tối giản của phân số là 3/2
"""

from math import *

a = input("Nhập chuỗi dạng a/b: ")
# phân tích chuỗi - tách tử số và mẫu số
a = a.split(('/'))
# Gán tử số và mẫu số cho hai biến tu_so và mau_so
tu_so = int(a[0])
mau_so = int(a[1])

## tim ra so lớn nhất mà cả từ và mẫu đều chia hết
def toi_gian(x, y):
    b = []
    for i in range(1, x+1):
        if x % i == 0 and y % i == 0:
            b.append(i)
    
    return b

day_so = sorted(toi_gian(tu_so, mau_so))

toi_gian = str(int(tu_so/day_so[-1])) + '/' + str(int(mau_so/day_so[-1]))

print(toi_gian)