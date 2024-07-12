scoreC = 100
scoreS = 100
for i in range(int(input())):
    c, s = map(int, input().split(' '))
    if c > s:
        scoreS -= c

    elif c < s:
        scoreC -= s

print(scoreC, scoreS, sep='\n')
