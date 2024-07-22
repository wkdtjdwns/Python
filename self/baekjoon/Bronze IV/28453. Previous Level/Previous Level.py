n = int(input())
levels = list(map(int, input().split(' ')))

result = [
    1 if level == 300 else
    2 if level >= 275 else
    3 if level >= 250 else
    4
    
    for level in levels
]

print(' '.join(map(str, result)))
