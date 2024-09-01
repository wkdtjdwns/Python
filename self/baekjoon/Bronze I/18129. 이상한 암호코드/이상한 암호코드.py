s, k = input().split(' ')
k = int(k)
s = s.lower()
n = len(s)
result = ''
temp = set()

i = 0
while i < n:
    c = s[i]
    cnt = 0

    while i < n and s[i] == c:
        cnt += 1
        i += 1

    if cnt >= k:
        if c not in temp:
            result += '1'
            temp.add(c)

    else:
        if c not in temp:
            result += '0'
            temp.add(c)

print(result)
