print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")

with open('a.txt', 'r', encoding='utf-8') as f:
    noidung = f.read()

# Tách tất cả các từ (chỉ lấy chữ cái, bỏ dấu câu)
import string
translator = str.maketrans('', '', string.punctuation)  # bỏ dấu câu
noidung_sach = noidung.translate(translator)

words = noidung_sach.split()

# Tìm độ dài từ dài nhất
max_len = len(max(words, key=len))

# Lấy tất cả các từ có độ dài = max_len
tu_dai_nhat = [word for word in words if len(word) == max_len]

print("Từ dài nhất trong file (độ dài:", max_len, "ký tự):")
for tu in tu_dai_nhat:
    print("→", tu)
