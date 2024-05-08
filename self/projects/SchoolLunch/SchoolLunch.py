import requests

# 함수 사용하기
def get_meals(dt):
    # 딕셔너리로 파라미터들을 할당해줌
    p = {
        'Type' : 'json',
        
        # 아래의 2 Key의 Value 값만 원하는 학교의 값으로 수정하면
        # 원하는 학교의 급식을 알 수 있음. 
        'ATPT_OFCDC_SC_CODE' : 'J10',
        'SD_SCHUL_CODE' : '7530167',
        
        'MLSV_YMD' : dt # 날짜만 바꿔줌
    }
    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo?' # ?는 없어도 됨
    result = requests.get(url, params=p) # url 주소를 전달함

    # try - except 문 : try 문에 있는 코드에 오류가 있는 지 검사하고 오류가 없으면 try 문에 있는 코드를 실행하고 오류가 있으면 except 문에 있는 코드를 실행함 (오류 검사)
    try:
        if result.status_code == 200:
            meals = result.json()

            return meals['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
            # return str(meal).replace('<br/>', '\n') - split 사용

        else: # 예외처리
            return ''

    except:
        return ''

date = input('알고 싶은 날짜 (yyyymmdd) : ')

meal = get_meals(dt=date)
if meal == '':
    print('자료가 없습니다.')

else:
    # split를 사용해 배열로 만든 후에 출력함
    meal = str(meal).split('<br/>')

    for i in meal:
        print(i)
