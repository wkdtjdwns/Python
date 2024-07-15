s = input()
sLength = len(s)
colon = s.count(':')
underBar = s.count('_')

print(sLength + colon + underBar * 5)
