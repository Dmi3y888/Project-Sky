print("Введите число")
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print("Ответ", a)
    else:
        print("Ответ", c)
else:
    if b > c:
        print("Ответ", b)
    else:
        print("Ответ", c)
