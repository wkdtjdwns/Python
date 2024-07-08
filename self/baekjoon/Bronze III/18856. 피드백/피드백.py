n = int(input())
result = [1, 2] + [i for i in range(3, 3 + n - 3)] + [997]

print(n)
print(*result)
