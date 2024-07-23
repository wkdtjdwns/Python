n = int(input())
a = [list(map(int, input().split(' '))) for _ in range(n)]
sort = sorted(a, key=lambda x:(-x[0], x[1], x[2]))

print(a.index(sort[0]) + 1)
