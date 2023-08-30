n, m = map(int, input().split())

basket = [i for i in range(1, n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    
    # temp 에 바구니(b) 값을 저장하고
    temp = basket[b - 1]
    
    # 바구니(b)를 바구니(a)로 바꾼 다음
    basket[b - 1] = basket[a - 1]
    
    # 바구니(a)를 temp 즉, 바구니(b)의 값으로 저장함
    basket[a - 1] = temp

print(*basket)
