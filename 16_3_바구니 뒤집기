n, m = map(int, input().split())

order = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    
    # i부터 j까지의 개수
    r = j - i + 1
    
# 1번부터 4번까지 뒤집는다고 하면 1번과 4번의 순서를 바꾸고
# 2번과 3번의 순서를 바꾸는 것과 같음
# 따라서 i부터 j까지의 개수(r)의 반만큼 반복문을 돌려 답을 구함
    for _ in range(r//2):
        temp = order[i-1]
    
    # i번째 바구니와 j번째 바구니의 위치를 서로 바꾼다.
        order[i-1] = order[j-1]
    
        order[j-1] = temp
    
    # i는 1 더하고 j는 1 빼서 반복문을 실행한다
        i += 1
        j -= 1

for o in order:
    print(o, end=' ')
