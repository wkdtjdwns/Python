a, b, c = sorted(map(int, input().split()))

d1 = b - a
d2 = c - b

if d1 == d2:
    if c + d2 < 100: print(c + d2)
    else: print(a - d2)

else:
    if d2 < d1: print(b - d2)
    else: print(c - d1)

print(d1, d2)
