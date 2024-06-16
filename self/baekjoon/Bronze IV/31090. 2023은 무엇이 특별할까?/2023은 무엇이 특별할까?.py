t = int(input())
for _ in range(t):
    year = input()
    n = year[2:]

    if (int(year) + 1) % int(n) == 0: print('Good')
    else: print('Bye')
