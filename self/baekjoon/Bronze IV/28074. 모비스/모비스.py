mobis = ['M', 'O', 'B', 'I', 'S']
input = input()
result = True

for i in mobis :
    if i not in input:
        result = False
        break

if result: print('YES')
else: print('NO')
