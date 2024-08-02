n, k = map(int, input().split(' '))
fk = k % 10
f2k = (2 * k) % 10
f = []

for i in range(1, n + 1):
    fx = i % 10
    if fx != fk and fx != f2k:
        f.append(str(i))
        
print(len(f))
print(' '.join(f))
