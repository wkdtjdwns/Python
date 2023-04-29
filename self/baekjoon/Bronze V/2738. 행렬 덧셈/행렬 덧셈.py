# 행렬을 받을 리스트 a, b 를 선언한다.
a, b = [], []

# n, m 을 통해 행렬의 크기를 입력 받는다.
n, m = map(int, input().split())

# a, b 에 행렬의 원소를 입력 받는다.
for i in range(n):
    i = list(map(int, input().split()))
    a.append(i)

for i in range(n):
    i = list(map(int, input().split()))
    b.append(i)

# 더해서 출력한다.    
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()
