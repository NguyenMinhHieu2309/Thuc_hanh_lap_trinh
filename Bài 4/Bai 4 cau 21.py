print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
data = input("Nhập các số nhị phân, cách nhau bởi dấu phẩy: ").split(',')
for b in data:
    if int(b, 2) % 5 == 0:
        print(b)
