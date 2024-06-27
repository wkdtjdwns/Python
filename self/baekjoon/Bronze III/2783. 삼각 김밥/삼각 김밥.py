x, y = map(int, input().split())
stores = [x / y]
for _ in range(int(input())):
    x, y = map(int, input().split(' '))
    stores.append(x / y)
    
print("%.2f" % (min(stores) * 1000))
