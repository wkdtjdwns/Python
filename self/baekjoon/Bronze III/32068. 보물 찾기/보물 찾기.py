for _ in range(int(input())):
    l, r, s = map(int, input().split(' '))
    ls = s - l
    rs = r - s
    if ls < rs: print(ls * 2 + 1)
    else: print(rs * 2)
