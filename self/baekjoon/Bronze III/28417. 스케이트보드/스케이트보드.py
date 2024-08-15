import sys
input = sys.stdin.readline

maxNum = 0
for _ in range(int(input())):
    sum = 0
    li = list(map(int, input().split(' ')))
    a = []
    b = []

    for j in range(2): a.append(li[j])
    for j in range(2, 7): b.append(li[j])

    a.sort()
    b.sort()

    sum += a[1] + b[3] + b[4]
    maxNum = max(maxNum, sum)

print(maxNum)
