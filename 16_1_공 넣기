N, M = map(int, input().split())

# 바구니 나열을 위해 basket 리스트를 만들고 N 만큼 요소를 초기화
basket = [0] * (N+1)

for _ in range(M):
    # 1번 바구니에서 j번 바구니까지 k 를 넣음 
    i, j, k = map(int, input().split())
    # 1번부터 j번까지 차례로 반복
    for n in range(i, j+1):
        # basket 리스트의 (n - 1)번째의 요소 = k
        basket[n] = k 


for i in range(1, N+1):
    # basket 리스트의 i번째 요소를 줄바꿈 없이 출력
    print(basket[i], end = ' ')
