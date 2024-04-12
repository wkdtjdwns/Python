n = int(input()) * 10

if n % 25 == 20 : print(n//25+2)
elif n % 25 == 15 or n % 25 == 10 or n % 25 == 5 : print(n//25+1)
else : print(n//25)
