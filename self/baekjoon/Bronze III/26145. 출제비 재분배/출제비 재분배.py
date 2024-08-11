n, m = map(int, input().split(' '))
s = list(map(int, input().split(' ')))
result = s + [0] * m

for i in range(n):
    money = list(map(int, input().split(' ')))
    for j in range(n + m):
        result[i] -= money[j]
        result[j] += money[j]

for i in result:
    print(i, end=' ')
