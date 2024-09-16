n = int(input())
word = {" ": 0}
for i in range(65, 91):
    word[chr(i).upper()] = word.setdefault(chr(i).upper(), i - 64)

for i in range(97, 123):
    word[chr(i).lower()] = word.setdefault(chr(i).lower(), i - 70)

secret = sorted(list(map(int, input().split(' '))))
plain = input()
arr = sorted([word.get(text) for text in plain])

print('y' if secret == arr else 'n')
