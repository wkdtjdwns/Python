h, w = map(int, input().split())

n = int(input())

A = [[0] * (w + 2) for i in range(0, h + 2, 1)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    A[x1][y1] += 1          
    A[x1][y2 + 1] -= 1       
    A[x2 + 1][y1] -= 1       
    A[x2 + 1][y2 + 1] += 1   

for i in range(1, h + 2):
    for j in range(1, w + 2):
        A[i][j] += A[i][j - 1]

for j in range(1, w + 2):
    for i in range(1, h + 2, 1):
        A[i][j] += A[i - 1][j]

for i in range(1, h + 1, 1):
    for j in range(1, w + 1, 1):
        print(A[i][j] % 2, end="")
        if j == w:
            print()
        else:
            print(" ", end="")
