n = int(input()) * 10
cnt = 0

while n > 0:
    if n >= 25: n -= 25
    elif n >= 15: n -= 15
    else: n -= 10
    cnt += 1

print(cnt)
