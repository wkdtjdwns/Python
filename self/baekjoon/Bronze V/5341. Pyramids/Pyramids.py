while True:
    blocks = 0
    n = int(input())
    for i in range(n, 0, -1):
        blocks += i
    if n == 0:
        break
    print(blocks)
