def check(a, op, b):
    if op == '>': return a > b
    elif op == '>=': return a >= b
    elif op == '<': return a < b
    elif op == '<=': return a <= b
    elif op == '==': return a == b
    elif op == '!=': return a != b

index = 1
while True:
    a, op, b = map(str, input().split(' '))
    if op == 'E': break
    print(f'Case {index}: {str(check(int(a), op, int(b))).lower()}')
    index += 1
