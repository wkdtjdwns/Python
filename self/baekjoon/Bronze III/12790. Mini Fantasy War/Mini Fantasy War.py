for _ in range(int(input())):
    a = list(map(int, input().split(' ')))
    s = [a[i] + a[i + 4] for i in range(4)]
    result = max(s[0], 1) + max(s[1], 1) * 5 + max(s[2], 0) * 2 + s[3] * 2
    
    print(result)