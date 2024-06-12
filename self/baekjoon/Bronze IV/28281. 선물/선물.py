n, x = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
price = []

for i in range(n - 1):
    price.append((a[i] + a[i + 1]) * x)

print(min(price))
