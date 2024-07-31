n, m = map(int, input().split(' '))
num = 1

for _ in range(n):
    for _ in range(m):
        if num % m == 0: print(num)
        else: print(num, end=' ')

        num += 1
