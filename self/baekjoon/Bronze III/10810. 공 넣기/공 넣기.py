n, m = map(int, input().split(' '))
balls = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split(' '))

    for b in range(i - 1 , j):
        balls[b] = k

print(*balls)
