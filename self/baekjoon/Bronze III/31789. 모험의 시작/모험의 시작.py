n = int(input())
x, s = map(int, input().split(' '))
weapon = [list(map(int, input().split(' '))) for _ in range(n)]
result = False
for c, p in weapon:
    if c <= x and p > s:
        result = True
        break
        
if result: print('YES')
else: print('NO')
