print("Введите количество членов")
a = int(input())
b = 1
c = (b/(b + 1))
while c <= a:
    c = b + c

print("Сумма первых", c)
