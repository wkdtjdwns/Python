max, result = 0, 0
snack = ['S', 'N', 'U']
for i in range(3):
    a, b = map(int, input().split(' '))
    cost, weight = a * 10, b * 10
    money = cost - 500 if cost >= 5000 else cost

    if (weight / money) > max:
        max = weight / money
        result = i

print(snack[result])
