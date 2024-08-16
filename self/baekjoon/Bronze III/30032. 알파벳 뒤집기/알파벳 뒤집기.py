n, d = map(int, input().split(' '))
for i in range(n):
    s = input()
    result = ""
    for j in range(n):
        if d == 1:
            if s[j] == 'd': result += 'q'
            elif s[j] == 'b': result += 'p'
            elif s[j] == 'q': result += 'd'
            else: result += 'b'

        else:
            if s[j] == 'd': result += 'b'
            elif s[j] == 'b': result += 'd'
            elif s[j] == 'q': result += 'p'
            else: result += 'q'

    print(result)
