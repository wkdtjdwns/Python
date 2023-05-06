hour, alcohol = map(int, input().split())
if (alcohol == 0) and (12 <= hour <= 16):
    print(320)
else:
    print(280)
