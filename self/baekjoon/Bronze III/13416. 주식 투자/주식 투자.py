for _ in range(int(input())):
    maxValue = 0
    for i in range(int(input())):
        a = list(map(int, input().split(' ')))
        
        if max(a) >= 0:
            maxValue += max(a)

    print(maxValue)
