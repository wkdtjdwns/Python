t = int(input())
for _ in range(t):
    nums = list(map(int, input().split(' ')))
    evenSum = 0
    minEven = 100
    for n in nums:
        if n % 2 == 0:
            evenSum += n
            if (minEven > n): minEven = n

    print(evenSum, end=' ')
    print(minEven)
