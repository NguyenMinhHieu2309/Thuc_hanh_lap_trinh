print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
ketqua = []
for i in range(1000, 3000):
    s = str(i)
    if all(int(ch) % 2 == 0 for ch in s):
        ketqua.append(s)
print(",".join(ketqua))
