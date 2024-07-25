n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
cnt = sum([(i + 1) // 2 for i in a])

print("YES" if cnt >= n else "NO")
