print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
import math

class Circle:
    def __init__(self, r=0):
        self.radius = r

    def getRadius(self):
        self.radius = float(input("Nhập bán kính: "))

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Sử dụng class
c = Circle()
c.getRadius()
print(f"Diện tích: {c.area():.2f}")
print(f"Chu vi: {c.perimeter():.2f}")
