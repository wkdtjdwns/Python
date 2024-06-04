li = []

for _ in range(6):
    li.append(int(input()))

abcd = sorted(li[:4]) 
ef = li[4:] 

print( sum(abcd[1:]) + max(ef) )
