while True:
    block = 0
    n = int(input())
    for i in range(n, 0, -1):
        block += i
    if n == 0:
        break
    print(block)
