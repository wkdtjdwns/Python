from datetime import datetime

current = datetime.strptime(input(), "%Y-%m-%d").date()
n = int(input())
cnt = 0
for _ in range(n):
    gift = datetime.strptime(input(), "%Y-%m-%d").date()
    if gift >= current:
        cnt += 1

print(cnt)
