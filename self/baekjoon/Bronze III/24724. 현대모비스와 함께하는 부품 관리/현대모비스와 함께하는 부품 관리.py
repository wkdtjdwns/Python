import sys

input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    a, b = map(int, input().split(' '))
    for _ in range(n):
        a, b = map(int, input().split(' '))

    print("Material Management " + str(i + 1))
    print("Classification ---- End!")
