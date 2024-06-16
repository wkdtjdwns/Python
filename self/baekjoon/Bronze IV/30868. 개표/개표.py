t = int(input())
for _ in range(t):
    n = int(input())
    result = ''
    
    for i in range(0, n):
        result += '|'
        if '|||||' in result:
            result = result.replace('|||||', '++++ ')

    print(result)
