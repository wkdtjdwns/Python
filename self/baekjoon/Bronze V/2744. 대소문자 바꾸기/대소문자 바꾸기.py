# if문
'''
r = ""
for s in input():
    if s.isupper():
        r += s.lower()
    else:
        r += s.upper()
print(r)
'''

# 삼항 연산자
r = ""
for i in input():
    r += i.upper() if i.islower() else i.lower()
print(r)
