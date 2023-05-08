import math
vacation = int(input())
vacation_korean = int(input())
vacation_math = int(input())
max_korean = int(input())
max_math = int(input())
# math.ceil() -> 소괄호() 안에 있는 값을 올림해줌
k = math.ceil(vacation_korean / max_korean)
m = math.ceil(vacation_math / max_math)
free = max(k, m)
print(vacation - free)
