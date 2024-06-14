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
pygame.display.set_caption("이미지 키보드 이벤트")

clock = pygame.time.Clock()

#---------------------------------이미지 붙이기 및 설정----------------------------------
snake_image = pygame.image.load("snake.png")
snake_rect = snake_image.get_rect() # snake_image의 영역을 가져오는 함수
snake_rect.topleft = (100, 100)

# 이미지 정가운데 맞춤
snake_rect.centerx = (WINDOW_WIDTH // 2)
snake_rect.bottom = (WINDOW_HEIGHT // 2)

#---------------------------------게임 실행 코드----------------------------------
running = True
while running:
    # 존재하는 모든 event들을 event 변수에 넣고
    for event in pygame.event.get():
        # event 변수의 값이 QUIT(나가기)라면
        if event.type == pygame.QUIT:
            # 실행을 멈춤
            running = False

    # 마우스를 클릭(좌클릭)했을 때
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x = event.pos[0] # 마우스의 x좌표를 받아옴
        mouse_y = event.pos[1] # 마우스의 y좌표를 받아옴

        # 마우스 클릭의 위치로 이미지를 이동 시킴
        snake_rect.centerx = mouse_x
        snake_rect.centery = mouse_y

    # 마우스가 드래그(좌클릭)되고 있을 때
    if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
        mouse_x = event.pos[0] # 마우스의 x좌표를 받아옴
        mouse_y = event.pos[1] # 마우스의 y좌표를 받아옴

        # 마우스의 위치로 이미지를 이동 시킴
        snake_rect.centerx = mouse_x
        snake_rect.centery = mouse_y

    # 움직이기 전에 배경을 검은색으로 채움. (이동한 다음에 남는 이미지를 없애기 위함)
    display_surface.fill((0, 0, 0))

    # 앞에서 검은색으로 채운 다음에 키보드 입력을 해서 바뀐 위치에 이미지를 화면에 붙임.
    display_surface.blit(snake_image, snake_rect) # 이미지를 화면에 붙이는 함수

    # 디스플레이 업데이트 (이게 없으면 위에 있는 코드들이 게임에 업데이트 되지 않아서 적용되지 않음)
    pygame.display.update()

    clock.tick(60) # 게임을 60 프레임으로 만듦

# 게임을 나감
pygame.quit()
```

---

![image](https://github.com/wkdtjdwns/Python/assets/128266768/e5e388dc-ccf8-4f7d-9f28-ca5b1ef7d90a)

![image](https://github.com/wkdtjdwns/Python/assets/128266768/8e832771-c047-43fc-818c-3a580f65e4f0)
