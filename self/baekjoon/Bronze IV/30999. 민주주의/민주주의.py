n, m = map(int, input().split(' '))
cnt = 0
for _ in range(n):
    str = input()
    result = str.count('O')

    if result > (m // 2):
        cnt += 1

print(cnt)
