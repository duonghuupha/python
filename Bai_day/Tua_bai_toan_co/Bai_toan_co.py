"""
Nhà An có một trang trại rộng lớn. Do ở thích cuuar An nên bố An chỉ nuôi gà và chó. Một hôm bố An đó con gái nhà nhà mình
nuôi bao nhiêu con gà, bao nhiêu con chó? Bố An cho biết nhà có tổng số gà và chó là x con. Do số lượng nhiều và khó đếm
từng loại nên An chỉ đếm được tổng số chân của gà và chó là y chân. Em hãy giúp an trả lời câu đó của bố.

Dữ liệu vào: đọc từ file văn bản TOANCO.INP gồm 2 số nguyên dương x, y trên một dòng. Hai số cách nhau một khoảng trống (x <= 10^5, y <= 4.10^5)

Kết quả: ghi ra file văn bản TOANCO.OUT gồm hai số tương ứng là số gà và số chó tìm được. Hai số cách nhau một khoảng trống.
"""
from math import *

file_in = open("./Tua_bai_toan_co/TOANCO.INP")
file_out = open("./Tua_bai_toan_co/TOANCO.OUT", "w")

s = file_in.readline()

s = s.split() # chuyển dạng chuỗi sang dạn mảng
tong = int(s[0]) # tổng số gà và chó
chan = int(s[1]) # tổng số chân của gà và chó

a = b = 0 # Gán giá trị cho hai biến a và b

""" 
Sử dụng vòng lặp for. Ta cho a chạy từ 1 tới tổng số gà và chó. Với mỗi giá trị a, ta có (tong - a) sẽ là số chó, từ đó  ta cộng số chân gà và số chân chó.
Nếu giá trị tính được là y (tổng số chân gà và chó) mà đề bài đã cho thì a và tong - a là số gà và số chó cần tìm 

"""
for a in range(tong):
    b = tong - a
    if (a  * 2 + b * 4) == chan:
        break # nếu thỏa điều kiện của IF thì dừng vòng lặp

file_out.write((str(a)) + " " + str(b))
file_in.close()
file_out.close()