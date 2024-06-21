import sys

n = int(sys.stdin.readline())
sum = 1
for i in range(n):
    sum += int(sys.stdin.readline())

print(sum - n)
