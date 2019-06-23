print("Введите сумму")
total = int(input())

if total > 1000:
    print("Вам скидка 5%")
    print("Сумма с скидкой", (total * 0.95))
elif total > 500:
    print("Вам скидка 3%")
    print("Сумма с скидкой", (total * 0.97))
else:
    print("Сумма без скидки", (total))