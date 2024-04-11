n = int(input())
cost = list(map(int, input().split()))
m, k = (map(int, input().split()))
one_set = k / m
cnt = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for l in range(j + 1, n):
            cur_sum = cost[i] + cost[j] + cost[l]
            if cur_sum <= one_set:
                cnt += 1

print(cnt)
