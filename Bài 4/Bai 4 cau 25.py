print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
ds = input("Nhập dãy số, cách nhau bằng dấu phẩy: ").split(',')
le = []
for so in ds:
    if int(so) % 2 != 0:
        le.append(so)
print("Các số lẻ là:", ",".join(le))
