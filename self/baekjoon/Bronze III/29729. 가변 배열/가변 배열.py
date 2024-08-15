import sys
input = sys.stdin.readline

s, n, m = map(int, input().split(' '))
cnt = 0
for _ in range(n + m):
    o = int(input())
    if o == 1:
        if s == cnt:
            s += s

        cnt += 1

    else:
        cnt -= 1

print(s)
