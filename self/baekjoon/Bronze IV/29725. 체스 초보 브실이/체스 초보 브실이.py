scores = {
    'K': 0,
    'P': 1,
    'N': 3,
    'B': 3,
    'R': 5,
    'Q': 9
}

black = 0
white = 0

for i in range(8):
    board = list(map(str, input()))

    for name in board:
        if name == '.':
            continue

        if name.isupper(): white += scores[name]
        else: black += scores[name.upper()]

print(white - black)
