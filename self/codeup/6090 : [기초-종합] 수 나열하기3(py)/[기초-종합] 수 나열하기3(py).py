a, m, d, n = map(int, input().split(' '))
result = a

for i in range(2, n+1):
    result *= m
    result += d

print(result)
