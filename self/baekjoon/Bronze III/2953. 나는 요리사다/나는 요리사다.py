scores = []
for _ in range(5):
    a, b, c, d = map(int, input().split(' '))
    scores.append(a + b + c + d)

print(scores.index(max(scores)) + 1, end=' ')
print(max(scores))
