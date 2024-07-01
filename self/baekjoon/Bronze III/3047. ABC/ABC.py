a, b, c = sorted(map(int, input().split(' ')))
index = input()
for s in index:
    if (s == 'A'): print(a, end=' ')
    elif (s == 'B'): print(b, end=' ')
    else: print(c, end=' ')
