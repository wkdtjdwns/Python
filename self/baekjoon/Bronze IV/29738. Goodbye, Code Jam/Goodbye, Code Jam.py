t = int(input())
for i in range(1, t + 1):
    n = int(input())
    round = 'Round 1'

    if n <= 25: round = 'World Finals'
    elif n <= 1000: round = 'Round 3'
    elif n <= 4500: round = 'Round 2'

    print(f'Case #{i}: {round}')
