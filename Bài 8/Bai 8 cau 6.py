print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import tkinter as tk
from tkinter import messagebox

# ==================== BƯỚC 1: Tạo cửa sổ và menu cơ bản ====================
def NewFile():
    messagebox.showinfo("Thông báo", "Bạn đã chọn New File!")

def OpenFile():
    messagebox.showinfo("Thông báo", "Bạn đã chọn Open!")

def ExitApp():
    if messagebox.askyesno("Thoát", "Bạn có chắc muốn thoát không?"):
        root.quit()

def InsText():
    messagebox.showinfo("Thông báo", "Bạn đã chọn Insert Text!")

def InsPic():
    messagebox.showinfo("Thông báo", "Bạn đã chọn Insert Picture!")

def About():
    messagebox.showinfo("About", "This is a simple example of a menu")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Menu Example - Bài 6 hoàn chỉnh")
root.geometry("500x350")

# Tạo thanh menu chính
menu = tk.Menu(root)
root.config(menu=menu)

# ==================== Menu File ====================
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()                    # đường kẻ ngang
filemenu.add_command(label="Exit", command=ExitApp)

# ==================== Menu Insert ====================
insertmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# ==================== Menu Help ====================
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# ==================== BƯỚC 2 & 3: Hiển thị giao diện đẹp ====================
# Thêm một nhãn lớn ở giữa để đẹp như hình mẫu
label = tk.Label(root, 
                 text="Chương trình có Menu hoàn chỉnh\n"
                      "Nhấn vào File / Insert / Help để thử!",
                 font=("Arial", 14),
                 fg="blue",
                 justify="center")
label.pack(expand=True)

# Chạy 
root.mainloop()
