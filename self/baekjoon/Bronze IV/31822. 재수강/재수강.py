subjectCode = input()[:5]
n = int(input())
cnt = 0
for _ in range(n):
    if input()[:5] == subjectCode: cnt += 1

print(cnt)
