""" 정석 풀이
m, n = map(int,input().split(' '))
grid = [[0 for _ in range(n)] for _ in range(m)]
direct = { 0:[0, 1], 1:[1, 0], 2:[0, -1], 3:[-1, 0] }

end = m * n - 2
cnt = 0
head = 0
i, j = 0, 0
grid[i][j] = "X"
while end >= 0:
    check = False
    if 0 <= i + direct[head][0] < m and 0 <= j + direct[head][1] < n:
        if grid[i + direct[head][0]][j + direct[head][1]] != "X":
            grid[i + direct[head][0]][j + direct[head][1]] = "X"
            i = i + direct[head][0]
            j = j + direct[head][1]
            check = True

    if not check:
        cnt += 1
        head = (head + 1) % 4
        i = i + direct[head][0]
        j = j + direct[head][1]
        grid[i][j] = "X"
        
    end -= 1
    
print(cnt)
"""

# 달팽이가 선을 꺾을 때 마다 가로, 세로 줄이 번갈아 가면서 1줄 씩 사라짐.
# 가로 혹은 세로 중 한 쪽이 완전히 사라지면 시행이 중단됨.
# 사라지는 줄의 수는 min(가로 줄 수, 세로 줄 수) * 2임
# 달팽이가 선을 꺾은 횟수는 사라진 줄 수 - 1임. (처음 시작할 때 1줄 먼저 지우고 시작하니까 1을 빼줘야 함)
# 만약 가로가 세로보다 길거나 같다면 1을 추가로 빼줘야 함.

m, n = map(int,input().split(' '))
print(2 * min(m, n) - 1 - (m <= n))
