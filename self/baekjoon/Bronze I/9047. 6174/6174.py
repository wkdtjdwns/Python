for _ in range(int(input())):
    num = int(input())
    cnt = 0
    while num != 6174:
        cnt += 1
        n = list(str(num))
        num = int(''.join(sorted(n, reverse=True))) - int(''.join(sorted(n)))
        
        if num < 1000:
            strNum = str(num)
            for _ in range(4 - len(strNum)):
                strNum += '0'

            num = int(strNum)

    print(cnt)
