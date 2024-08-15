import datetime
import sys
input = sys.stdin.readline

year, month, day = map(int, input().split('-'))
day += int(input())
month += (day - 1) // 30
day = (day - 1) % 30 + 1
year += (month - 1) // 12
month = (month - 1) % 12 + 1

time = datetime.datetime(year, month, day)
print(time.strftime('%Y-%m-%d'))
