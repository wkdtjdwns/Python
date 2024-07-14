a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = a * p
y = b if c >= p else b + (p - c) * d
print(min(x, y))
