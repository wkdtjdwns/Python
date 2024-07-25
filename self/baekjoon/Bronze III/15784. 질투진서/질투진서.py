n, a, b = map(int, input().split(' '))
seats = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    seat = list(map(int, input().split(' ')))
    for j in range(n):
        seats[i][j] = seat[j]

target = seats[a - 1][b - 1]
for i in range(n):
    if target < seats[a - 1][i] or target < seats[i][b - 1]:
        print('ANGRY')
        exit()

print('HAPPY')
