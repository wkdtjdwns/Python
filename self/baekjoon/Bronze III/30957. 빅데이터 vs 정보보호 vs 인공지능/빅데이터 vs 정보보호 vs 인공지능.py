n = int(input())
b = s = a = 0
for i in input():
    if i == "B": b += 1
    elif i == "S": s += 1
    else: a += 1

if b == s and s == a and b == a:
    print("SCU")

else:
    if b == max(b, s, a): print("B", end="")
    if s == max(b, s, a): print("S", end="")
    if a == max(b, s, a): print("A", end="")
