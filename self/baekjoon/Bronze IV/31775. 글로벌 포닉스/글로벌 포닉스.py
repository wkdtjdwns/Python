isStartL = False
isStartK = False
isStartP = False

for _ in range(3):
    s = input()

    if s[0] == 'l': isStartL = True
    elif s[0] == 'k': isStartK = True
    elif s[0] == 'p': isStartP = True

if isStartL and isStartK and isStartP: print('GLOBAL')
else: print('PONIX')
