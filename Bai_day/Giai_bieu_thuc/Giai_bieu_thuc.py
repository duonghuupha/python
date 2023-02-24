# Giải biểu thức (TP Vũng tàu 2020)
# Cho 3 số nguyên dương a, b, c
# Yêu cầu: Tính giá trị của biểu thức
# S = a^2 + b^2 + c^2 / abc + căn bậc hai của abc
# Dữ liệu vào: File ROOT.INP chứa 3 số nguyên dương a,b,c. Mỗi số trên một dòng
# Kết quả: Ghi vào file RÔT.OUT kết quả S tính được (làm tròn lấy 2 chữ số sau phần thập phân)


from math import * ## nhập dữ thư viện toán học

# open(filename, mode)  hàm open để mở file; filename là đường dẫn file cần mở; mode là phương thức thao tác trên tệp
# w là tạo một file mới để ghi, nếu file đã tồn tại thì ghi dữ liệu mới
# e là mở file chỉ để đọc
# r+ là mở file để đọc và ghi
# w+ là Tạo một file mới để đọc và ghi , nếu fle đã tồn tại thì sẽ bị ghi mới
# a là mở một file để ghi thêm vào cuối file,, nếu không tìm thấy file sẽ tạo file mới
# a+ là mở một file để đọc và ghi thêm vào cuối fule nếu không tìm thấy sẽ tạo một file mới

file_in = open("./Giai_bieu_thuc/ROOT.INP")
file_out = open("./Giai_bieu_thuc/ROOT.OUT", "w")

a = file_in.readline() ## đọc dữ liệu theo dòng
b = file_in.readline()
c = file_in.readline()

a = int(a) ## ép  kiểu dữ liệu thành kiểu số nguyên (int - interger)
b = int(b)
c = int(c)

tu = a**2 + b**2 + c**2 # Toán tủ ** là toán tử mũ a**n
mau = a*b*c

s = tu/mau + sqrt(mau) ## sprt là toán tử tính căn bậc hai

s = str(round(s, 2)) ## làm tròn lấy 2 số sau phần thập phân

file_out.write(s) ## Ghi kết quả vào file