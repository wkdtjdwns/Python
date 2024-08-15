import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split(' ')))
cur = 0
result = 0
for i in a:
    if i > 0:
        cur += 1
        result = max(result, cur)

    else:
        cur = 0

print(result)
