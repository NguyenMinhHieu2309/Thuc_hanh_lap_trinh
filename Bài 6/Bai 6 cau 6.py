print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
class MyString:
    def __init__(self):
        self.str1 = ""  

    def get_String(self):
        self.str1 = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.str1.upper())

# Sử dụng class
obj = MyString()
obj.get_String()
obj.print_String()
