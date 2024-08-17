def factorial(n):
    if n < 1: return 1
    return n * factorial(n - 1)

def getResult(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) / (factorial(k) * factorial(n - k))

print(int(getResult(int(input()), 5)))
