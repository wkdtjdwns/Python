n = int(input())

sea = []
for _ in range(n): sea.append(list(map(int, input().split(" "))))

max_catch = 0

for i in range(n - 1):
    for j in range(n - 1):
        # 2 * 2의 범위 계산
        max_catch = max(max_catch, sea[i][j] + sea[i][j + 1] + sea[i + 1][j] + sea[i + 1][j + 1])

print(max_catch)
