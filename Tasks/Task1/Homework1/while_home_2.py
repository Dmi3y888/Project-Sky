print("Введите количество членов")
a = float(input())
print("а =", a)
n = int(input())
print("n =", n)
i = 0
c = a
while i < n:
    i = i + 1
    c = c * (a - i * n)

print("Результат", c)

# a(a-n)(a-2n)  …(a-n*n)
