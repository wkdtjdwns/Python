n, k = map(int, input().split())
result = 0
cnt = [0, 0, 0, 0, 0, 0, 0]
cost = [1000, 1000, 2000, 3000, 3000, 6000, 6000]
for i in range(n):
    a = list(map(int, input().split()))[1:]
    for j in a:
        cnt[j - 1] += 1

for i in range(len(cnt)):
    if cnt[i] >= k:
        result += cost[i]

print(result * n)
