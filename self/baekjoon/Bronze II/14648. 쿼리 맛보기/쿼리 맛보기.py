n, q = map(int, input().split(' '))
board = list(map(int, input().split(' ')))
for qq in range(q):
    query = list(map(int, input().split(' ')))

    if query[0] == 1:
        print(sum(board[query[1] - 1:query[2]]))
        board[query[1] - 1], board[query[2] - 1] = board[query[2] - 1], board[query[1] - 1]
        
    else:
        print(sum(board[query[1] - 1:query[2]]) - sum(board[query[3] - 1:query[4]]))
