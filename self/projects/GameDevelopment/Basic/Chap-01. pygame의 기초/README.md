```python
#---------------------------------게임 개발의 기본 설정----------------------------------
import pygame # Python을 활용한 게임 개발을 위한 라이브러리

# pygame을 사용하기 위한 초기화
pygame.init()

#---------------------------------게임 창에 대한 설정----------------------------------
# 게임 창의 크기 설정
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

# 게임 창의 크기 적용 (가로, 세로)
# display_suface = pygame.display.set_mode((600, 300))도 가능하지만 비추천
display_suface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 창의 타이틀 설정
pygame.display.set_caption("Hello World!")

#---------------------------------게임 실행 코드----------------------------------
running = True
while running:
    # 존재하는 모든 event들을 event 변수에 넣고
    for event in pygame.event.get():
        # event 변수의 값이 QUIT(나가기)라면
        if event.type == pygame.QUIT:
            # 실행을 멈춤
            running = False

# 게임을 나감
pygame.quit()
```

---

![image](https://github.com/wkdtjdwns/Python/assets/128266768/ccab4d6a-8224-4613-9d36-c13c295c6b4b)
