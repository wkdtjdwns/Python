v = int(input())
s = input()

a = b = 0
for i in range(v):
    if s[i] == 'A': a +=1
    else: b += 1

if a > b: print('A')
elif a < b: print('B')
else: print('Tie')
