cnt = 0
for _ in range(int(input())):
    s = input()
    if '01' in s or 'OI' in s:
        cnt += 1

print(cnt)
