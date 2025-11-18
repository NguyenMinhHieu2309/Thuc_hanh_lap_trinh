print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
print("Sinh viên: Nguyễn Minh Hiếu")
print("Mssv: 245752021610010")
print("*" * 50)

class Bank:
    Account_type = "Savings"
    Bank_location_type = "SBI ATM Machine"

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance

    def __repr__(self):
        print("=" * 45)
        print("     CHÀO MỪNG BẠN ĐẾN VỚI ATM PYTHON")
        print("=" * 45)
        self.dang_nhap()
        return ""

    def dang_nhap(self):
        while True:
            try:
                pin = int(input("\nNhập mã PIN (gợi ý: 123): "))
                if pin == 123:
                    print(f"\nĐăng nhập thành công! Xin chào {self.name}")
                    self.menu()
                    break
                else:
                    print("Sai PIN! Vui lòng thử lại.")
            except:
                print("Chỉ được nhập số thôi nhé!")

    def menu(self):
        while True:
            print("\n" + "="*35)
            print("1. Xem số dư")
            print("2. Rút tiền")
            print("3. Nạp tiền")
            print("4. Thoát")
            print("="*35)
            try:
                chon = int(input("Chọn chức năng (1-4): "))
                if chon == 1: self.xem_sodu()
                elif chon == 2: self.rut_tien()
                elif chon == 3: self.nap_tien()
                elif chon == 4:
                    print("\nCảm ơn bạn đã sử dụng dịch vụ!")
                    print("Hẹn gặp lại!")
                    break
                else:
                    print("Chỉ chọn từ 1-4 thôi!")
            except:
                print("Nhập sai rồi! Chỉ nhập số 1-4!")

    def xem_sodu(self):
        print(f"\nSố dư hiện tại: {self.balance:,} VND")

    def rut_tien(self):
        try:
            tien = int(input("\nNhập số tiền muốn rút: "))
            if tien <= 0:
                print("Số tiền phải > 0!")
            elif tien > self.balance:
                print("Số dư không đủ!")
            else:
                self.balance -= tien
                print(f"Rút thành công {tien:,} VND")
                print(f"Số dư mới: {self.balance:,} VND")
        except:
            print("Nhập số hợp lệ!")

    def nap_tien(self):
        try:
            tien = int(input("\nNhập số tiền muốn nạp: "))
            if tien <= 0:
                print("Số tiền phải > 0!")
            else:
                self.balance += tien
                print(f"Nạp thành công {tien:,} VND")
                print(f"Số dư mới: {self.balance:,} VND")
        except:
            print("Nhập số hợp lệ!")


