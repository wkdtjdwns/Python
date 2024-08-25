n = int(input())
for _ in range(n):
    print('G' * n, end='')
    print('.' * (3 * n), end='')
    print()

for _ in range(n):
    print('.' * n, end='')
    print('I' * n, end='')
    print('.' * n, end='')
    print('T' * n, end='')
    print()

for _ in range(n):
    print('.' * (2 * n), end='')
    print('S' * n, end='')
    print('.' * n, end='')
    print()
