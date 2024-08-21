n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
level = 0
result = 0
for i in a:
    level += i
    if level < 0: level = 0
    if level >= m: result += 1
    
print(result)
