def checkPrime(n):
    isPrime = True
    for i in range(2, n):
        if n % i == 0: isPrime = False

    return isPrime

n = int(input())
nums = list(map(int, input().split(' ')))

cnt = 0
for i in nums:
    if i == 1:
        continue

    if checkPrime(i):
        cnt += 1

print(cnt)
