n = int(input())
s = input()
security = (len(s) - len(s.replace('security', ''))) / 8
bigdata = (len(s) - len(s.replace('bigdata', ''))) / 7
if security > bigdata: print('security!')
elif security < bigdata: print('bigdata?')
else: print('bigdata? security!')
