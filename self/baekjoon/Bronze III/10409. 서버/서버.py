n, t = map(int, input().split(' '))
process = list(map(int, input().split(' ')))
total = 0
cnt = 0
for i in range(n):
    if total + process[i] > t:
        break

    total += process[i]
    cnt += 1

print(cnt)
