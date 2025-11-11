print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
str_input = input("Enter a String: ")
dict_count = {}

for n in str_input:
    if n in dict_count.keys():
        dict_count[n] += 1
    else:
        dict_count[n] = 1

print(dict_count)
