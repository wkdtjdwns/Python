for _ in range(int(input())):
    result = 0
    n = int(input())
    nums = list(map(int, input().split(' ')))

    for i in nums:
        result += i;

    print(result)
