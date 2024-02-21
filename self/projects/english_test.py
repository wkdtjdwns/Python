import random # random 라이브러리를 가져옴
from gtts import gTTS # 'gtts' 라이브러리 중에서 'gTTS' 부분만 가져옴
import playsound # 'playsound' 라이브러리를 가져옴

# 문제 배열 (문제가 될 단어들만 적어 놓으면 됨)
problems = []

# 문제 배열의 순서를 섞어서 랜덤한 문제가 나오도록 함
random.shuffle(problems)

problem_num = 0  # 문제 번호

# tts들 초기화
problem_num_ttses = [] # 번호 tts
problem_ttses = [] # 단어 tts

# 문제들의 개수에 따라서 임시로 'ㅇ', 'd'으로 된 tts들을 배열에 추가
for i in range(len(problems)):
    problem_num_ttses.append(gTTS('ㅇ', lang='ko'))
    problem_ttses.append(gTTS('d', lang='en'))

# 문제가 모두 끝날 때까지 반복
while problem_num < len(problems):
    # 문제를 낼지 말지 결정 (아무런 키나 입력하기 | 다시 듣고 싶으면 'r' 또는 'R'입력하기)
    q = input("다음 문제를 내시겠습니까? (아무런 키나 입력해주세요 | 문제를 다시 듣고 싶다면 'r' 또는 'R'을 입력해 주세요) ")

    # q 변수에 무언가라도 입력되었는지 확인
    if q != '':

        # 다시 듣고 싶을 때
        if q == 'r' or q == 'R':
            # 문제 번호를 줄이고
            problem_num -= 1
            # 플레이만 함 (이미 저장은 되어 있기 때문)
            playsound.playsound(f'problem_num_{problem_num}.mp3')
            playsound.playsound(f'problem_{problem_num}.mp3')

        # 다음 문제를 듣고 싶을 때
        else:
            # 추가되었던 tts들의 내용을 바꾸어서 재생시키도록 함
            # 참고 - 1개의 mp3 파일을 재사용 했을 때 오류가 생겨서 서로 다른 이름의 mp3 파일을 생성한 후 재생시킴
            problem_num_ttses[problem_num] = gTTS(f'{problem_num + 1}번', lang='ko')  # 문제 번호
            problem_num_ttses[problem_num].save(f'problem_num_{problem_num}.mp3')  # 'problem_num_n.mp3'로 저장
            playsound.playsound(f'problem_num_{problem_num}.mp3')  # 'problem_num_n.mp3' 재생

            problem_ttses[problem_num] = gTTS(problems[problem_num], lang='en')  # 문제 단어
            problem_ttses[problem_num].save(f'problem_{problem_num}.mp3')  # 'problem_n.mp3'로 저장
            playsound.playsound(f'problem_{problem_num}.mp3')  # 'problem_n.mp3' 재생

        # 문제 번호 증가
        problem_num += 1

        # 초기화
        q = ''
