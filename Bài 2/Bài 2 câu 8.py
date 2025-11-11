print("Sinh vien: Nguyen Minh Hieu")
print("Mssv: 245752021610010")
print("*************************************")
a, b = 1, 2
total = 0
print(a, end=" ")

while a <= 4000000:
    if a % 2 == 0:
        total += a
    print(a, end=" ")
    a, b = b, a + b

print("\nTổng các số chẵn trong dãy Fibonacci nhỏ hơn 4.000.000 là:", total)
