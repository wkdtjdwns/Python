import sys
input = sys.stdin.readline

n = int(input())
temp = []
temp.append(int(input()))

for i in range(n):
    a, b = map(int, input().split())
    temp.append(temp[i] + a - b)

for i in range(n + 1):
    if temp[i] < 0:
        print(0)
        exit()

print(max(temp))
