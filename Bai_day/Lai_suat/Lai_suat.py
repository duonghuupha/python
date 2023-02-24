"""
Một người gửi tiền vào nggan hàng có kỳ hạn là c tháng với lãi xuất mỗi tháng là k% số tiền gửi ban đầu là A
Tính số tiền người đó nhận được sau t tháng. Biết rằng tiền lãi mỗi tháng được cộng dồng vào tiền gốc, nếu nhận 
tiền trước kỳ hạn thì số tiền được tính với lãi xuất không kỳ hạn là h% của số tiền bạn đầu A nhân với số tháng đã gửi.
Trong trường hợp rút tiền sau kỳ hạn thì số tháng sau kỳ hạn sẽ tính với lãi xuất không kỳ hạn là h%, các số tiền thu được
đã qua kỳ hạn

Dữ liệu vào: Tiệp vưn bản BL2.INP ghi 5 số kỳ hạn (c, nếu c = 0 là gửi không kỳ hạn), thời gian gửi (t). số tiền ban đầu (A),
lãi xuất có kỳ hạn (k), lãi xuất không kỳ hạn (h), các số cách nhau một ký tự trắng
Dữ liệu ra: Tệp văn bản BL2.OUT ghi 1 số tiền nhận được (kết quả làm trong đến 1 số lẻ sau dấu chấm thập phân)
Ví dụ:
BL2.INP
12 13 100 1.0 0.2
BL2.OUT
112.9
--------------------
BL2.INP
0 10 100 1.0 0.2
BL2.OUT 
102.0
"""
## Phân tích dữ liệu ví dụ đề bài
"""
c = 12 - kỳ hạn 
t = 13 - số tháng gửi (đúng kỳ hạn 12 tháng và vượt kỳ hạn 1 tháng)
A = 100 - Số tiền ban đầu
k = 1.0 - Lãi xuất gửi nếu rút tiền đúng kỳ hạn
h = 0.2 - Lãi xuất gửi nếu rút không đúng kỳ hạn
Trong trường hợp trên khách hàng gửi kỳ hạn 12 tháng và gửi 13 tháng sau mới rút
vậy khách hàng khi rút tiền sẽ được tính lãi của một kỳ theo kỳ hạn và 1 tháng không đúng kỳ hạn
A = 100
A1 = (100*0.01)*12
A2 = (100*0.002)*1
A_T = A + A1 + A2
---------------------------------------------------------------------------------
c = 0 - Kỳ hạn: Không có kỳ hạn
t = 10
A = 100
k = 1.0
h = 0.2
Trong trường hợp trên khách hàng gửi không kỳ hạn nếu lãi được tính theo lãi không kỳ hạn (0.2)
A = 100
A1 = (100*0.002) * 10
A_T = A + A1
"""

from math import *

## Đọc dữ liệu từ hai file
file_in = open('./Lai_suat/BL2.INP')
file_out = open('./Lai_suat/BL2.OUT', 'w')

du_lieu = file_in.readline()
du_lieu = du_lieu.split(' ')

c = int(du_lieu[0])
t = int(du_lieu[1])
A = int(du_lieu[2])
k = float(du_lieu[3])
h = float(du_lieu[4])

## kiểm tra kỳ hạn có hay không
s = 0
if c == 0: # gửi không có kỳ hạn
    s = A + ((A * (h / 100)) * t)
else: ## có kỳ hạn
    ## kiểm tra gửi bao nhiêu tháng
    if c > t: # rút tiền trước kỳ hạn
        s = A + ((A * (h / 100)) * t)
    elif c == t: ## rút đúng kỳ hạn
        s = A + ((A * (k / 100)) * t)
    else: ## rút tiền sau kỳ hạn
        s1 = A + ((A * (k / 100)) * c)
        s = s1 + ((s1 * (h / 100)) * (t - c))

s = str(s)
file_out.write(s)
file_in.close()
file_out.close()