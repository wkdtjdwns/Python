result = 0
for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    result += b % a

print(result)
