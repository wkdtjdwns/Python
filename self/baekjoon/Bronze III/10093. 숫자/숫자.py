a, b = map(int, input().split(' '))
if a > b:
    a, b = b, a

cnt = b - a - 1
if a == b or a + 1 == b:
    cnt = 0

print(cnt)
print(*range(a + 1, b))
