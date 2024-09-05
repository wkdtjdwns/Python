for _ in range(int(input())):
    y1 = 0
    k1 = 0
    for _ in range(9):
        y2, k2 = map(int, input().split(' '))
        y1 += y2
        k1 += k2

    if y1 > k1: print('Yonsei')
    elif y1 < k1: print('Korea')
    else: print('Draw')
