n = int(input())
a = list(map(int, input().split(' ')))
ok, no, hmm = 0, 0, 0

for i in a:
    if i == 1: ok += 1
    elif i == -1: no += 1
    else: hmm += 1

if hmm >= n / 2: print('INVALID')
elif ok > no: print('APPROVED')
else: print('REJECTED')
