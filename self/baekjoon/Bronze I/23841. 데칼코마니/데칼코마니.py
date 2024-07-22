n, m = map(int, input().split(' '))
graph = []
for i in range(n):
    a = list(input())
    for j in range(m // 2):
        if a[j] != '.':
            a[m - j - 1] = a[j]

        elif a[m - j - 1] != '.':
            a[j] = a[m - j - 1]

    graph.append(a)

for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j], end='')

    print()
