"""
Minh đố An: Cho một số chẵn K, hãy tìm hai số nguyên tố sao cho tổng của chúng bằng số chẵn K đã cho.
Dữ liệu vào: Tệp NT.INP
Dòng đầu tiên chứa số nguyên dương N tương ứng số lần test
N dòng tiếp theo, mỗi dòng chứa một số K
Kết quả: Tệp văn bản NT.OUT gồm N dòng tương ứng N kết quả. Mỗi kết quả hiển thị tổng hai số nguyên tố bằng số K nhập vào
Ví dụ:
NT.INP       NT.OUT
2            8 = 5 + 3
8            24 = 19 + 5
24
"""

from math import *

file_in = open('./Nguyen_to/NT.INP')
file_out = open('./Nguyen_to/NT.OUT', 'w')

du_lieu = file_in.readlines() ## Đọc dữ liệu từ file và đưa vào LIST

N = int(du_lieu[0]) ## lấy ra số lần test
du_lieu.pop(0) ## xóa phần tử N

# hàm kiểm tra tính nguyên tố của một số
def nguyento(x): # x là số được duyệt trong khoảng từ A đến B + 1
    if x  == 1:
        return False # Nếu x  = 1 thì trả về False vì 1 không phải là số nguyên tố
    for i in range (2, int(sqrt(x)) + 1): # duyệt các số t 2 đến căn bậc hai của x + 1
        if x % i == 0: # Nếu số x chia hết cho i thì trả về False (vì số x chia hết cho 1 và chính nó lại chia hết cho số i thì không phải là số nguyên tố)
            return False # trả về False
    return True # Nếu chạy hết vòng lặp mà không sai thì trả về True

def tong_nt(x):
    a = 0
    b = 0
    for a in range(x):
        b = x - a
        if nguyento(b) and nguyento(a):
            if b + a == x:
                return str(a) + '-' + str(b)
                break
        

s = []
for item in du_lieu:
    N_test = int(item)
    data = tong_nt(N_test)
    data = data.split('-')
    s .append(str(N_test) + ' = ' + data[0] + '+' + data[1])

for item in s:
    file_out.write(item + '\n')

file_in.close()
file_out.close()
