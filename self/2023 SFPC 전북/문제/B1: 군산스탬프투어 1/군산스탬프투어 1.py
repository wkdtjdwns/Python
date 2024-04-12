n, m, k, t = map(int, input().split())
A =  list(map(int, input().split()))

ans = 0
for i in range(k):
    cnt = 5
    B =list(map(int, input().split()))
    for j in B:
        cnt += (A[j-1 ] + 5)
    if cnt <= t:
        ans += 1

print(ans)
