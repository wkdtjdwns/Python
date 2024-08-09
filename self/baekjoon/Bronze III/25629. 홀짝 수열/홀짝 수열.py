import math
n = int(input())
li = list(map(int, input().split(' ')))
a = 0
b = 0
for i in range(len(li)):
    if li[i] % 2 != 0: a += 1
    else: b += 1

if a == math.ceil(n / 2) and b == n // 2: print(1)
else: print(0)
