maxValue = 0
for _ in range(int(input())):
    a, d, g = map(int, input().split(' '))

    if a == (d + g): score = 2 * a * (d + g)
    else: score = a * (d + g)

    if score > maxValue: maxValue = score

print(maxValue)
