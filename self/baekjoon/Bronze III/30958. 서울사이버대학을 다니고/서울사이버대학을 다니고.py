n = int(input())
s = input()
alphabet = [0 for _ in range(26)]
for i in s:
    if i == ' ' or i == ',' or i == '.': continue
    alphabet[ord(i) % 97] += 1

print(max(alphabet))
