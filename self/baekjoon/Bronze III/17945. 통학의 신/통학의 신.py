a, b = map(int, input().split(' '))
li = []
for i in range(-1000, 10001):
    if i * (2 * a - i) == b:
        li = list(set([-i, -(2 * a - i)]))

print(*sorted(li))
