A = [1, 2, 3, 4, 5]
A.append(6)
B = A
print(B)

tong = 0
for item in B:
    tong += int(item)
print(tong)

C  = []
for item in B:
    if int(item) % 2 == 0:
        C.append(int(item))
print(C)

del(C[0])
print(C)