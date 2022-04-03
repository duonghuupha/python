import math

# function check enter character is number interger
def numinput(msg):
    while True:
        try:
            number = int(input(msg))
        except ValueError:
            print("Not an interger! Try again.")
            continue
        else:
            return number
            break

a = numinput("Nhap vao so can tim boi so: ")
b = numinput("Nhap vao gioi han cac boi so can tim: ")

## tim boi so cua so nhap vao
c = []
for i in range(b):
    if i % a == 0:
        c.append(i)
    
print(c)

