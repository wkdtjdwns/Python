n, m = map(int, input().split(' '))
result = 0
maxResult = 0
zebra = []
for i in range(n):
    zebra.append(list(map(int, input())))
    cnt = 0
    if zebra[i][0]:
        cnt += 1

    for j in range(1, m):
        if zebra[i][j - 1] == 0 and zebra[i][j] == 1:
            cnt += 1

    if maxResult < cnt:
        maxResult = cnt
        result = 1

    elif maxResult == cnt:
        result += 1

print(maxResult, result)
