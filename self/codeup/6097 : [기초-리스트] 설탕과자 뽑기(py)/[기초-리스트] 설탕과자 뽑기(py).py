board = []
w, h = map(int, input().split(' '))
for i in range(w):
  board.append([])
  for j in range(h):
    board[i].append(0)

n = int(input())

for _ in range(n):
  l, d, x, y = map(int, input().split(' '))

  for k in range(l):
    if d == 0:
      board[x - 1][y - 1] = 1
      y += 1

    else:
      board[x - 1][y - 1] = 1
      x += 1

for i in range(w):
  for j in range(h):
    print(board[i][j], end=' ')

  print()
