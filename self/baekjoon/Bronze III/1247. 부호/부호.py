from sys import stdin

for _ in range(3):
    n = int(stdin.readline())
    result = 0
    for _ in range(n): result += int(stdin.readline())
    if result == 0: print(0)
    elif result > 0: print('+')
    else: print('-')
