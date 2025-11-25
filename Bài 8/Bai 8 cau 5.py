print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import tkinter as tk

# ================== Tạo cửa sổ chính ==================
root = tk.Tk()
root.title("Choose your favourite programming language")
root.geometry("380x300")

# Biến để lưu lựa chọn
v = tk.IntVar()
v.set(1)    # giá trị mặc định là Python

# Danh sách ngôn ngữ
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm hiển thị lựa chọn
def ShowChoice():
    print("Bạn đã chọn:", v.get())
    # Có thể thêm Label để hiển thị kết quả trên giao diện nếu muốn

# Tiêu đề
tk.Label(root, 
         text="Choose your favourite programming language:",
         justify=tk.LEFT,
         font=("Arial", 12, "bold"),
         pady=20).pack(anchor=tk.W, padx=20)

# ================== PHẦN a) Dùng Radiobutton bình thường ==================
# (Bạn có thể bỏ comment phần này nếu muốn so sánh)
# for lang, val in languages:
#     tk.Radiobutton(root, text=lang, variable=v, value=val, command=ShowChoice).pack(anchor=tk.W, padx=40)

# ================== PHẦN b) Dùng indicatoron=0 → nút tròn như hình ==================
for val, language in enumerate(languages):  # val = 0,1,2,3,4
    tk.Radiobutton(root,
                   text=language[0],          # tên ngôn ngữ
                   indicatoron=0,             # ← Quan trọng: biến thành nút tròn
                   width=20,
                   padx=20,
                   pady=5,
                   variable=v,
                   command=ShowChoice,
                   value=language[1]).pack(anchor=tk.W, padx=30)

# Nút thoát (tùy chọn)
tk.Button(root, text="Thoát", command=root.quit, bg="red", fg="white").pack(pady=20)

# Chạy chương trình
root.mainloop()
