a = 1
b = 0.1
c = 1
while a + b <= 9.9:
    c = c * (a + b)
    print(c)

    a = a + 1
    b = b + 0.1  #a(a-n)(a-2n)…(a-n*n)