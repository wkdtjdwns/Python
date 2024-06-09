```python
#---------------------------------게임 개발의 기본 설정----------------------------------
import pygame

import pygame.docs # Python을 활용한 게임 개발을 위한 라이브러리

# pygame을 사용하기 위한 초기화
pygame.init()

#---------------------------------게임 창에 대한 설정----------------------------------
# 게임 창의 크기 설정
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# RGB 색상 기준으로 사용할 색상을 정의함.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 게임 창의 크기 적용 (가로, 세로)
# display_suface = pygame.display.set_mode((600, 300))도 가능하지만 비추천
display_suface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 창의 타이틀 설정
pygame.display.set_caption("Hello World!")

# 백그라운드 색상 설정
display_suface.fill(BLUE)

#---------------------------------도형 그리기 코드----------------------------------

# line 함수를 이용한 라인 그리기
# pygame.draw.line(surface, 색상, (시작 위치), (끝 위치), 선 크기)
pygame.draw.line(display_suface, RED, (100, 100), (200, 200), 3)

# circle() 함수를 이용한 원 그리기
# pygame.draw.circle(surface, 색상, (위치), 크기(지름), 선 크기) / (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2) = 게임의 정중앙
pygame.draw.circle(display_suface, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 50, 3)

# rect() 함수를 이용한 사각형 그리기
# pygame.draw.rect(surface, 색상, (시작 위치, 상대 위치), 선 크기)
pygame.draw.rect(display_suface, GREEN, (300, 0, 100, 100), 3)

#---------------------------------게임 실행 코드----------------------------------
running = True
while running:
    # 존재하는 모든 event들을 event 변수에 넣고
    for event in pygame.event.get():
        # event 변수의 값이 QUIT(나가기)라면
        if event.type == pygame.QUIT:
            # 실행을 멈춤
            running = False

    # 디스플레이 업데이트 (이게 없으면 위에 있는 코드들이 게임에 업데이트 되지 않아서 적용되지 않음)
    pygame.display.update()

# 게임을 나감
pygame.quit()
```

---

![image](https://github.com/wkdtjdwns/Python/assets/128266768/de8acf01-43c5-4018-bd20-e0192780f157)
