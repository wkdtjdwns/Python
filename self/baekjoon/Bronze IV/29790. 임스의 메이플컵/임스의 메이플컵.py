n, u, l = map(int, input().split(' '))
isBaekjoon = False
isMaple = False

if n >= 1000: isBaekjoon = True
if (u >= 8000) or (l >= 260): isMaple = True

if (isBaekjoon) and (isMaple): print('Very Good')
elif isBaekjoon: print('Good')
else: print('Bad')
