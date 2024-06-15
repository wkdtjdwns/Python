#---------------------------------게임 개발의 기본 설정----------------------------------
import pygame

import pygame.docs # Python을 활용한 게임 개발을 위한 라이브러리

# pygame을 사용하기 위한 초기화
pygame.init()

#---------------------------------게임 창에 대한 설정----------------------------------
# 게임 창의 크기 설정
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 색상 설정
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("텍스트 표시")

clock = pygame.time.Clock()

#---------------------------------이미지 붙이기 및 설정----------------------------------
snake_image = pygame.image.load("snake.png")
snake_rect = snake_image.get_rect() # snake_image의 영역을 가져오는 함수

# 이미지 정가운데 맞춤
snake_rect.centerx = (WINDOW_WIDTH // 2)
snake_rect.bottom = (WINDOW_HEIGHT // 2)

mouse_image = pygame.image.load("mouse.png")
mouse_rect = mouse_image.get_rect()
mouse_rect.centerx = (WINDOW_WIDTH // 2)
mouse_rect.bottom = (WINDOW_HEIGHT // 3)

#---------------------------------게임 실행 코드----------------------------------
running = True
while running:
    # 존재하는 모든 event들을 event 변수에 넣고
    for event in pygame.event.get():
        # event 변수의 값이 QUIT(나가기)라면
        if event.type == pygame.QUIT:
            # 실행을 멈춤
            running = False

    keys = pygame.key.get_pressed() # key가 눌러졌을 때 발생하는 이벤트 감지

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and snake_rect.left > 0: snake_rect.x -= 5
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and snake_rect.right < WINDOW_WIDTH: snake_rect.x += 5

    # y좌표는 위로 갈 수록 -이고, 아래로 갈 수록 +임.
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and snake_rect.top > 0: snake_rect.y -= 5
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and snake_rect.bottom < WINDOW_HEIGHT: snake_rect.y += 5

    # 이미지 충돌 이벤트 구현
    if snake_rect.colliderect(mouse_rect):
        print('충돌')

    # 움직이기 전에 배경을 검은색으로 채움. (이동한 다음에 남는 이미지를 없애기 위함)
    display_surface.fill((0, 0, 0))

    # 앞에서 검은색으로 채운 다음에 키보드 입력을 해서 바뀐 위치에 이미지를 화면에 붙임.
    display_surface.blit(snake_image, snake_rect) # 이미지를 화면에 붙이는 함수
    display_surface.blit(mouse_image, mouse_rect) # 이미지를 화면에 붙이는 함수

    # 디스플레이 업데이트 (이게 없으면 위에 있는 코드들이 게임에 업데이트 되지 않아서 적용되지 않음)
    pygame.display.update()

    clock.tick(60) # 게임을 60 프레임으로 만듦

# 게임을 나감
pygame.quit()
