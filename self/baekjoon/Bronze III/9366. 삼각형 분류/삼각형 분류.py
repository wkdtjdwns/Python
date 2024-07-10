for i in range(int(input())):
    abc = sorted(map(int, input().split(' ')))
    print(f"Case #{i + 1}: ", end='')
    if abc[0] + abc[1] <= abc[2]: print("invalid!")
    elif abc[0] == abc[1] == abc[2]: print("equilateral")
    elif abc[0] == abc[1] or abc[1] == abc[2] or abc[2] == abc[0]: print("isosceles")
    else: print("scalene")
