n = int(input())
x = 0
y = 0
for _ in range(n):
    win = input()
    if (win == 'D'): x += 1
    else: y += 1

    if abs(x - y) >= 2:
        break

print(x, y, sep=':')
