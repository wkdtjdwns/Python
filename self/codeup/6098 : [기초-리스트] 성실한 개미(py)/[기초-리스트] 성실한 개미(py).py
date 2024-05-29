d = []
for i in range(12):
    d.append([])
    for j in range(12):
        d[i].append(0)

for i in range(10):
    a = input().split()
    for j in range(10):
        d[i + 1][j + 1] = int(a[j])

x = y = 2
while True:
    if d[x][y] == 0:
        d[x][y] = 9
        
    elif d[x][y] == 2:
        d[x][y] = 9
        break

    if (d[x][y + 1] == 1 and d[x + 1][y] == 1) or (x == 9 and y == 9):
        break

    if d[x][y + 1] != 1:
        y += 1
        
    elif d[x + 1][y] != 1:
        x += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(d[i][j], end=' ')
    print()
