alphabet = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
}

t = int(input())

for _ in range(t):
  s = set(input())
  a = alphabet - s
  sum = 0

  for i in a: sum += ord(i)

  print(sum)
