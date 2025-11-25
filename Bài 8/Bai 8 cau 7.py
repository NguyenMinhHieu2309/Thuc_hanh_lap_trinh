print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

import tkinter as tk
import random

# ==================== BIẾN TOÀN CỤC ====================
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
timeleft = 120          # Bước 2: đổi thành 120 giây (theo yêu cầu)

# ==================== HÀM ĐẾM NGƯỢC ====================
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        e.config(state='disabled')
        label.config(text="Game Over!\nFinal Score: " + str(score), fg="red", font=("Helvetica", 30))

# ==================== HÀM CHỌN MÀU TIẾP THEO ====================
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()
        # Nếu người chơi gõ đúng tên MÀU HIỂN THỊ (không phải chữ màu)
        if e.get().lower() == colours[1].lower():
            score += 2                    # Bước 3: đúng +2 điểm
        else:
            if e.get():                   # có gõ nhưng sai → trừ 1 điểm
                score -= 1                # Bước 3: sai -1 điểm

        e.delete(0, tk.END)
        random.shuffle(colours)
        
        # Hiển thị màu chữ là colours[1], nhưng nội dung chữ là colours[0]
        label.config(fg=colours[1], text=colours[0], font=("Helvetica", 60))
        
        scoreLabel.config(text="Score: " + str(score))

# ==================== HÀM BẮT ĐẦU TRÒ CHƠI ====================
def startGame(event):
    if timeleft == 120:          # chỉ bắt đầu đếm ngược lần đầu
        countdown()
    nextColour()

# ==================== TẠO GIAO DIỆN ====================
root = tk.Tk()
root.title("COLOURGAME")
root.geometry("500x500")
root.configure(bg="lightyellow")

# Hướng dẫn
instructions = tk.Label(root, text="Type in the COLOUR of the words, and not the word text!",
                        font=('Helvetica', 14), bg="lightyellow")
instructions.pack(pady=10)

# Điểm số
scoreLabel = tk.Label(root, text="Press Enter to start", font=('Helvetica', 18), bg="lightyellow")
scoreLabel.pack()

# Thời gian còn lại
timeLabel = tk.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 18), bg="lightyellow")
timeLabel.pack(pady=10)

# Từ màu hiển thị (chữ to)
label = tk.Label(root, font=('Helvetica', 60), bg="lightyellow")
label.pack(pady=50)

# Ô nhập liệu
e = tk.Entry(root, font=('Helvetica', 20), justify='center')
e.pack(pady=20)
e.focus_set()

# Bắt phím Enter để bắt đầu
root.bind('<Return>', startGame)

# Chạy chương trình
root.mainloop()
