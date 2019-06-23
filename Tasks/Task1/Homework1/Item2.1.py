print("Введите сумму")
total = int(input())
if total > 1000:
    print("Вам скидка 10%", (total * 0.9))
else:
    print("Сумма без скидки", (total))
