n = int(input())
minY = 99999999999999999999999999999999999999999999
maxY = -999999999999999999999999999999999999999999
for _ in range(n):
    x, y = map(int, input().split(' '))
    minY = min(minY, y)
    maxY = max(maxY, y)

print(maxY - minY)
