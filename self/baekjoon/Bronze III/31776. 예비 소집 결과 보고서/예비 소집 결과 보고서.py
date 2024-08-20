n = int(input())
result = 0
for _ in range(n):
    solve = list(map(int, input().split(' ')))

    if sum(solve) == -3:
        continue

    for i in range(3):
        if solve[i] == -1:
            solve[i] = 121

    if solve[0] <= solve[1] <= solve[2]:
        result += 1

print(result)
