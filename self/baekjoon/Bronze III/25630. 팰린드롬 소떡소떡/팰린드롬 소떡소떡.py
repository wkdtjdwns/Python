n = int(input())
st = list(input())
cnt = 0
for i in range(n // 2):
    if st[i] != st[-1 - i]:
        cnt += 1

print(cnt)
