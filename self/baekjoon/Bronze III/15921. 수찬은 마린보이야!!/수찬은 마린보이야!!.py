n = int(input())
if n == 0:
    print("divide by zero")
else:
    # 사실 답은 항상 1.00인데...
    a = list(map(int, input().split(' ')))
    result = sum(a) / n / (sum(a) / n)
    print("%.2f" % result)
