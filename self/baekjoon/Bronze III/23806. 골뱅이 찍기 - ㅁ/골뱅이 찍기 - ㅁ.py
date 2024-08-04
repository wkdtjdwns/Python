n = int(input())
for _ in range(n):
    print('@' * (n * 5))

for _ in range(n * 3):
    print('@' * n, end='')
    print(' ' * (n * 3), end='')
    print('@' * n)

for _ in range(n):
    print('@' * (n * 5))
