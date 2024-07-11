for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    candies = list(map(int, input().split(' ')))
    result = 0

    for i in candies:
        result += i // k
    
    print(result)
