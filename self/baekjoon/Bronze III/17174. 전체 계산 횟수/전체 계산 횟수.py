n, m = map(int, input().split(' '))
t = n

while n:
    n //= m
    t += n

print(t)
