print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

from tkinter import *

# ================== a) Xây dựng cửa sổ đồ họa window form ==================
window = Tk()
window.title("Welcome to LikeGeeks app")    # Tiêu đề cửa sổ
window.geometry("350x200")                  # Kích thước cửa sổ
# ===========================================================================

# ================== b) Thêm một widget (Button) vào window form ============
lbl = Label(window, text="Hello", font=("Arial Bold", 18))
lbl.grid(column=0, row=0, padx=30, pady=40)   # Đặt Label vào lưới
# ===========================================================================

# ================== c) Xây dựng phương thức xử lý sự kiện phím bấm =========
def clicked():
    lbl.configure(text="Button was clicked !!")
# ===========================================================================

# ================== d) Thay đổi màu nền (bg) và màu chữ (fg) của button ====
btn = Button(window,
             text="Click Me",
             command=clicked,        # Gọi hàm clicked khi nhấn
             bg="orange",            # ← Câu d: Màu nền button
             fg="white",             # ← Câu d: Màu chữ button
             font=("Helvetica", 12, "bold"),
             padx=20,
             pady=10)
btn.grid(column=1, row=0)       # Đặt Button vào lưới
# ===========================================================================

# Chạy chương trình
window.mainloop()
