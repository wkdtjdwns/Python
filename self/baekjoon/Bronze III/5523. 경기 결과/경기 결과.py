from sys import stdin

winA = 0
winB = 0
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split(' '))
    if (a > b): winA += 1
    elif (a < b): winB += 1

print(winA, winB)
