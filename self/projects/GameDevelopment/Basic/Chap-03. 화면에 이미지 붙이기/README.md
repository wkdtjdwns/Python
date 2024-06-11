# [무료 아이콘 사이트 (상업 목적으로 사용 가능)](https://iconarchive.com/)

```python
#---------------------------------게임 개발의 기본 설정----------------------------------
import pygame

import pygame.docs # Python을 활용한 게임 개발을 위한 라이브러리

# pygame을 사용하기 위한 초기화
pygame.init()

#---------------------------------게임 창에 대한 설정----------------------------------
# 게임 창의 크기 설정
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("이미지 붙이기")

#---------------------------------이미지 붙이기 및 설정----------------------------------
snake_image = pygame.image.load("snake.png")
snake_rect = snake_image.get_rect() # snake_image의 영역을 가져오는 함수
snake_rect.topleft = (100, 100)

#---------------------------------게임 실행 코드----------------------------------
running = True
while running:
    # 존재하는 모든 event들을 event 변수에 넣고
    for event in pygame.event.get():
        # event 변수의 값이 QUIT(나가기)라면
        if event.type == pygame.QUIT:
            # 실행을 멈춤
            running = False

    display_surface.blit(snake_image, snake_rect) # 이미지를 화면에 붙이는 함수

    # 디스플레이 업데이트 (이게 없으면 위에 있는 코드들이 게임에 업데이트 되지 않아서 적용되지 않음)
    pygame.display.update()

# 게임을 나감
pygame.quit()
```

---

## [사용한 이미지](https://www.iconarchive.com/show/square-animal-icons-by-martin-berube/Snake-icon.html)

![image](https://github.com/wkdtjdwns/Python/assets/128266768/56b6fa7f-668b-4235-8235-fd88f197323f)
