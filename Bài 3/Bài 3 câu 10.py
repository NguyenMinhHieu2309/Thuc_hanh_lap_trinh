print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")

import math
R = float(input("Nhap ban kinh R: "))
def Tinh(R):
    
    if R <= 0:
        print("Ban kinh phai lon hon 0!")
    else:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R**2
        print("Chu vi hinh tron =", chu_vi)
        print("Dien tich hinh tron =", dien_tich)
        
Tinh(R)
