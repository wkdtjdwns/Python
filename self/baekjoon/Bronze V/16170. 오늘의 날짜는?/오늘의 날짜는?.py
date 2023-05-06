from datetime import datetime, timedelta
# 우리나라는 세계 표준 시(UTC+0)를 기준보다 9시간 앞서있기 때문에, timedelta 메소드를 통해 9를 빼줌
now = datetime.now() - timedelta(hours=9)
print(now.year)
# 출력형식을 맞추기 위함
print('%02d' % now.month)
print('%02d' % now.day)
