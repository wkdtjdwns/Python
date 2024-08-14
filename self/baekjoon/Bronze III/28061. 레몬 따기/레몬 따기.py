n = int(input())
x = list(map(int, input().split(' ')))

result = 0
for i, lemon in enumerate(x, 1):
    temp = lemon - (n + 1 - i)
    result = max(result, temp)
    
print(result)
