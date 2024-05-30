info1, math1, kor1, eng1 = map(int, input().split(' '))
info2, math2, kor2, eng2 = map(int, input().split(' '))

result1 = info1 + math1 + kor1 + eng1
result2 = info2 + math2 + kor2 + eng2

print( max(result1, result2) )
