"""
Để động viên thành tích học tập xuất sắc của các em học sinh trong năm học 2019-2020, thầy giáo chủ nhiệm chuẩn bị các món quà
được đánh số từ 1 đến n. Sau đó thầy giáo sẽ cho các em  lên bốc thăm để nhận món quà may mắn.
Đầu tiên thây giáo sẽ ghi tất cả các số nguyên lẻ từ 1 đến n, sau đó sé ghi tất cả các số nguyên chẵn từ 2 đến n (theo thứ tự tăng
dần) để tạo thành một dãy số phần thưởng.
Mỗi bạn sẽ bốc thăm một số k ứng với con số của món quà mình đạt được.
Yêu cầu: IN ra số của món quà học sinh đạt được
Dữ liệu vào: Dòng du nhất ghi số nguyên n và k
Dữ liệu ra: In ra số của món quà mà học sinh đạt được

SOMAYMAN.INP
10 6
SOMAYMAN.OUT
2
"""

from math import *

file_in = open('./So_may_man/SOMAYMAN.INP')
file_out = open('./So_may_man/SOMAYMAN.OUT', 'w')

dulieu = file_in.readline()
dulieu = dulieu.split(' ')

n = int(dulieu[0])
k = int(dulieu[1])

## liệt kê các số lẻ trong khoảng n
so_le = []
for i in range(1, n+1):
    if i % 2 != 0:
        so_le.append(i)

## Liệt kê các số chẵn trong khong n
so_chan = []
for j in range(2, n + 1):
    if j % 2 == 0:
        so_chan.append(j)

day_so_thuong = so_le + so_chan

file_out.write(str(day_so_thuong[k-1]))

file_in.close()
file_out.close()