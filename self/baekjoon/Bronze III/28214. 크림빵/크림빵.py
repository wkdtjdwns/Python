n, k, p = map(int, input().split(' '))
B = list(map(int, input().split(' ')))
result = 0

for i in range(n):
    b = B[i * k:i * k + k]
    if k - sum(b) < p:
        result += 1

print(result)
