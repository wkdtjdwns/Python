for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split(' ')))
    minValue = min(nums)
    maxValue = max(nums)

    print(minValue, end=' ')
    print(maxValue)
