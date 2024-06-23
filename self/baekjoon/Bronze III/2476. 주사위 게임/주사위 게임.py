n = int(input())
total = []
for _ in range(n):
    a, b, c = map(int, input().split(' '))
    if a == b == c: total.append(10000 + a * 1000)
    elif a == b: total.append(1000 + a * 100)
    elif a == c: total.append(1000 + a * 100)
    elif b == c: total.append(1000 + b * 100)
    else: total.append(100 * max(a, b, c))

print(max(total))
