h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))
A =[]

for i in range(6):
    B = list(map(int,input().split()))
    A.append(B)
    

t = h2 * 60 + m2 - h1 * 60 - m1

min1 = 24 * 60 + 10

for i1 in range(1, 6):
    for i2 in range(1, 6):
        for i3 in range(1, 6):
            for i4 in range(1, 6):
                for i5 in range(1, 6):
                    if len({i1, i2, i3, i4, i5}) == 5:
                        total = A[0][i1] + A[i1][i2] + A[i2][i3] + A[i3][i4] + A[i4][i5] + A[i5][0]
                        if total < min1:
                            min1 = total

t = t - min1
print(f"{t//60:02d}:{t%60:02d}")
