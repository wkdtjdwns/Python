import sys
input = sys.stdin.readline

n, t = input().split()
name = set()
for _ in range(int(n)):
    name.add(input())

p = len(name)
if t == 'Y': print(p)
elif t == 'F': print(p // 2)
else: print(p // 3)
