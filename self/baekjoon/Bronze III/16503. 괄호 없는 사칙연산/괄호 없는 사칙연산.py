def calc(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return -1 * (abs(a) // abs(b)) if a * b < 0 else a // b

ko = list(map(str, input().split(' ')))
ko[0] = int(ko[0])
ko[2] = int(ko[2])
ko[4] = int(ko[4])

a = calc(calc(ko[0], ko[2], ko[1]), ko[4], ko[3])
b = calc(ko[0], calc(ko[2], ko[4], ko[3]), ko[1])
print(min(a, b))
print(max(a, b))
