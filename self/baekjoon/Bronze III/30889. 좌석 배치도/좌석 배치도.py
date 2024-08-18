seats = []
for i in range(10):
    seats.append(list('.' for i in range(20)))

for i in range(int(input())):
    seat = input()
    x = ord(seat[0])
    y = int(seat[1:])

    seats[x % 65][y - 1] = 'o'

for i in range(10):
    for j in range(20):
        print(seats[i][j], end='')

    print()
