cost = [0] * 1001
jin = 0
cnt = 0
for i in range(int(input())):
    d, c = map(str, input().split(' '))
    c = int(c)

    if d == 'jinju': jin = c
    elif c > 1000: cnt += 1
    else: cost[c] += 1

for i in range(jin + 1, 1001):
    cnt += cost[i]

print(jin)
print(cnt)
