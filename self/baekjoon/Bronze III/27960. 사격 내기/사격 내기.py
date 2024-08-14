a, b = map(int, input().split(' '))
binA = bin(a)
binB = bin(b)

result = int(bin(a ^ b)[2:], 2)
print(result)
