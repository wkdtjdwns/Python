n = int(input())
cnt = 0
for _ in range(n):
    D, x = map(str, input().split('-'))

    if int(x) <= 90:
        cnt += 1

print(cnt)
