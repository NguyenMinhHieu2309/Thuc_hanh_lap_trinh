print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
def benefit(t, n, k):
   
    if t < 0 or n <= 0 or k <= 0:
        print("Du lieu khong hop le!")
    else:
      
        money = n * (1 + t/100)**k
        print("So tien nhan duoc sau", k, "thang la", round(money, 2))

t = float(input("Nhap lai suat theo thang: "))
n = float(input("Nhap so von ban dau: "))
k = int(input("Nhap so thang gui tien: "))

benefit(t, n, k)
