chess = [1, 1, 2, 2, 2, 8] # 원래 필요한 피스 수
piece = list(map(int, input().split())) # 지금 가지고 있는 피스 수
for j in range(6):
    # 원래 체스에 필요한 피스의 개수에 지금 가지고 있는 피스의 개수를 뺌
    print((chess[j] - piece[j]), end = ' ') 
