defense, armor_pen = map(int, input().split())
if (int(defense - (defense * armor_pen / 100))) >= 100:
    print("0")
else:
    print("1")
