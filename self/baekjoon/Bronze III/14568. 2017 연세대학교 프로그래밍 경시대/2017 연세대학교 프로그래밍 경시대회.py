n = int(input())
result = 0
for i in range(2, n-1, 2):
    result += (n - i - 2) // 2

print(result)
