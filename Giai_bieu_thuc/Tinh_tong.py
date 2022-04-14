""""
Viết chương trình nhập vào 2 số nguyên A và B (0 < A < B)
a. Tìm và tính tổng các số nguyên tố của dãy số từu A đến B
b. Xuất ra màn hình các số chia hết cho 5 ccuar dãy số từ A đến B.
Ví dụ: Nhập A = 6, B = 22
Kết quả tổng các số nguyên tố trong dãy số từ 6 đến 22 là:
    7 + 11 + 13 + 17 + 19 = 67
Các số chia hết cho 5 của dãy số từ 6 đến 22 là: 10, 15, 20
"""

from math import *

a = input("Nhập vào số nguyên A: ")
b = input("Nhập vào số nguyên B: ")

a = int(a)
b = int(b)
tong = 0 # Gán tổng bẳng 0
s = "" # Gán chuỗi rỗng
5
# số nguyên tố hay hợp số là số chỉ chia hết cho 1 và chính nó

# hàm kiểm tra tính nguyên tố của một số
def nguyento(x): # x là số được duyệt trong khoảng từ A đến B + 1
    if x  == 1:
        return False # Nếu x  = 1 thì trả về False vì 1 không phải là số nguyên tố
    for i in range (2, int(sqrt(x)) + 1): # duyệt các số t 2 đến căn bậc hai của x + 1
        if x % i == 0: # Nếu số x chia hết cho i thì trả về False (vì số x chia hết cho 1 và chính nó lại chia hết cho số i thì không phải là số nguyên tố)
            return False # trả về False
    return True # Nếu chạy hết vòng lặp mà không sai thì trả về True

for i in range(a, b+ 1):
    if nguyento(i):
        tong += i # Tính tổng các số nguyên tố
    if i % 5 == 0:
        s += str(i) + ", "

print(tong, " ", s[:len(s) - 2])