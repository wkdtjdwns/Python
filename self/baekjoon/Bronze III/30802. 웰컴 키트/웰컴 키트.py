n = int(input())
size = list(map(int, input().split(' ')))
t, p = map(int, input().split(' '))
tBundle = 0
for i in size:
    if i == 0: continue
    if i <= t: tBundle += 1
    elif i % t == 0: tBundle += i // t
    else: tBundle += i // t + 1

pBunble = n // p
pen = n % p

print(tBundle)
print(pBunble, pen)
