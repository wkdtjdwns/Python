n = int(input())
# 정수형으로 변환시키지 않으면 실수형으로 출력됨
print(int(n * 0.78), end = " ")
print(int(n * 0.8 + (n * 0.2 * 0.78)))
