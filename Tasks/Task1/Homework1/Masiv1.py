x = [1, 2, 3, 4, 5, 6, 7]
a = float(input())
b = float(input())
s = 0
k = 1
mi = 1000
ma = 0

for e in x:
    if e < a:
        s = s + e

    if e > b:
        k = k * e

    if a <= e <= b:
        ma = max([ma, e])
        mi = min([mi, e])

print(ma)
print(mi)
print(s)
print(k)
