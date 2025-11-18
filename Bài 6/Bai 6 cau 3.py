print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
class Nguoi(object):
    def getGender(self):
        return "Unknown"


class Nam(Nguoi):
    def getGender(self):
        return "Nam"


class Nu(Nguoi):
    def getGender(self):
        return "Nữ"


aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
