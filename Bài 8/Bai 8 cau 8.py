print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ==================== a) Hiển thị thông tin cá nhân ====================
def show_info():
    ho_ten = "Nguyễn Minh Hieu"                  # Thay bằng tên bạn
    ngay_sinh = "23/09/2006"                  # Thay bằng ngày sinh bạn
    mssv = "245752021610010"                         # Thay bằng MSSV bạn
    lop = "65K1"                         # Thay bằng lớp bạn

    info = f"Họ và tên: {ho_ten}\n" \
           f"Ngày sinh: {ngay_sinh}\n" \
           f"MSSV: {mssv}\n" \
           f"Lớp: {lop}"
    
    messagebox.showinfo("Thông tin sinh viên", info)

# ==================== b) Xử lý nút Click Me + RadioButton ====================
def click_me():
    # Lấy giá trị được chọn từ RadioButton
    choice = var.get()
    
    if choice == 1:
        result = "Bạn đã chọn số 1 (First)"
    elif choice == 2:
        result = "Bạn đã chọn số 2 (Second)"
    elif choice == 3:
        result = "Bạn đã chọn số 3 (Third)"
    else:
        result = "Bạn chưa chọn số nào!"
    
    messagebox.showinfo("Kết quả lựa chọn", result)

# ==================== TẠO GIAO DIỆN ====================
root = tk.Tk()
root.title("Welcome")
root.geometry("400x200")
root.configure(bg="lightcyan")

# Biến lưu lựa chọn RadioButton
var = tk.IntVar()
var.set(1)  # mặc định chọn First

# Nhóm RadioButton
frame_radio = tk.Frame(root, bg="lightcyan")
frame_radio.pack(pady=30)

tk.Radiobutton(frame_radio, text="First", variable=var, value=1, bg="lightcyan", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_radio, text="Second", variable=var, value=2, bg="lightcyan", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_radio, text="Third", variable=var, value=3, bg="lightcyan", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

# Nút Click Me
btn = tk.Button(root, text="Click Me", command=click_me, font=("Arial", 12, "bold"), bg="orange", fg="white", width=12)
btn.pack(pady=10)

# ==================== a) Gọi thông tin khi khởi động (tự động hiện) ====================
root.after(500, show_info)   # hiện hộp thoại thông tin sau 0.5 giây khi mở chương trình

# Chạy chương trình
root.mainloop()
