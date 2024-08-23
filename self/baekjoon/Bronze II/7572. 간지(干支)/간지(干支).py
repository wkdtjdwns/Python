a = 'ABCDEFGHIJKL'
b = '0123456789'
n = int(input()) - 2013
print(a[(n + 5) % 12] + b[(n - 1) % 10])
