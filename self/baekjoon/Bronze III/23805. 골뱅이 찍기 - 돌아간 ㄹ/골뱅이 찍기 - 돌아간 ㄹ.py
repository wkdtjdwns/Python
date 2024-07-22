n = int(input())
for i in range(n):
    print('@@@' * n + ' ' * n + '@' * n)

for j in range(3 * n):
    print('@' * n + ' ' * n + '@' * n + ' ' * n + '@' * n)

for k in range(n):
    print('@' * n + ' ' * n + '@@@' * n)
