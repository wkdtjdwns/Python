for _ in range(int(input())):
    a, b, c, d, e = map(float, input().split(' '))
    result = (a * 350.34) + (b * 230.90) + (c * 190.55) + (d * 125.30) + (e * 180.90)

    print('${:.2f}'.format(result))
