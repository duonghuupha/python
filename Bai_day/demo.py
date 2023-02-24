a = [1,2,3,4,5]
""" 
Them phan tu vao mang
"""
a.append(6)
print(a)
"""
Do dai cua mang
"""
print()
print(len(a))
"""
Hien ti phan tu 3 trong mang
"""
print()
print(a[3])
"""
Hiein thi phan tu co gia tri 3 trong mang
"""
print()
def hien_thi_phan_tu(a, b):
    phan_tu = 0
    for i in a:
        if i == b:
            phan_tu = i
    return phan_tu

if hien_thi_phan_tu(a, 3) == 3:
    print(hien_thi_phan_tu(a, 3))
else:
    print('Khong co phan tu nao bang 3')
"""
CHuyeun mang thanh chuoi 
"""
print()
string = ''
for i in a:
    string += str(i)+','
print(string)
"""
Xoa phan tu thu 2 trong mang
"""
print()
del a[2]
print(a) 