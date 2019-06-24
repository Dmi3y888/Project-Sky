print("Введите количество членов")
a = float(input("Введи а - "))
n = int(input("Введи n - "))
i = 0
c = a
while i < n:
    i = i + 1
    c = c * (a - i * n)

print("Результат", c)

# a(a-n)(a-2n)  …(a-n*n)
