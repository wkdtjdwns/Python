n = int(input())
for i in range(2):
    for _ in range(n):
        print('@' * n, end='')
        print(' ' * (n * (3 - i)), end='')
        print('@' * n)

for _ in range(n):
    print('@' * (n * 3))

for i in range(1, -1, -1):
    for _ in range(n):
        print('@' * n, end='')
        print(' ' * (n * (3 - i)), end='')
        print('@' * n)
