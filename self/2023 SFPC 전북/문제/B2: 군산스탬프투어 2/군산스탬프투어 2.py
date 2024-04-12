n, m, t = map(int, input().split())
A = [0] + list(map(int, input().split()))

e = n ** m
ans = 0

for i in range(e):
    a = i
    max1 = 0
    C = [0] * (n + 1)
    B = [0] * (m + 1)

    for j in range(1, m + 1):
        pp = a % n + 1
        B[j] = pp
        C[pp] += 1
        max1 = max(max1, C[pp])
        a //= n
        
    if max1 == 1:
        cnt = 5
        for j in range(1, m + 1):
            cnt += A[B[j]] + 5
        if cnt <= t:
            ans += 1

print(ans)
