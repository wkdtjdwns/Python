#---------------------------------게임 개발의 기본 설정----------------------------------
import pygame
import random

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

# 쥐의 방향을 바꿔주기 위한 변수
mouse_dx = 5
mouse_dy = 5

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("이미지 충돌과 점수판 만들기")

clock = pygame.time.Clock()
live = 5
scores = 0

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

banana_image = pygame.image.load("banana.png")
banana_rect = banana_image.get_rect()
banana_rect.centerx = WINDOW_WIDTH
banana_rect.bottom = (WINDOW_HEIGHT // 2)


system_font = pygame.font.SysFont('verdanai', 30)

game_live = system_font.render("Lives: " + str(live), True, GREEN, BLACK)
game_live_rect = game_live.get_rect()
game_live_rect.topleft = (10, 10)

score_font = pygame.font.SysFont('verdanai', 30)

game_score = system_font.render("Scores: " + str(scores), True, GREEN, BLACK)
game_score_rect = game_score.get_rect()
game_score_rect.topleft = (10, 30)

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
        live -= 1

        # 충돌하면 쥐의 위치를 랜덤으로 이동시킴
        mouse_rect.x = random.randint(0, WINDOW_WIDTH - 50)
        mouse_rect.y = random.randint(0, WINDOW_HEIGHT - 50)

    # 쥐가 자동으로 움직이게 함.
    mouse_rect.x = mouse_rect.x + mouse_dx
    mouse_rect.y = mouse_rect.y + mouse_dy

    # 쥐의 방향을 바꿔줌.
    if mouse_rect.x > WINDOW_WIDTH or mouse_rect.x < 0:
        mouse_dx *= -1

    if mouse_rect.y > WINDOW_HEIGHT  or mouse_rect.y < 0:
        mouse_dy *= -1

    # 바나나가 왼쪽 화면으로 넘어가게 되면 스코어 1점 감점
    # 바나나는 x좌표 -10만큼 계속 움직임
    if banana_rect.x < 0:
        scores -= 1
        banana_rect.x = WINDOW_WIDTH + 50
        banana_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    
    else:
        banana_rect.x -= 10 

    # 점수판 표시
    if live > 0:
        game_live = system_font.render("Lives: " + str(live), True, GREEN, BLACK)

    else:
        game_live = system_font.render("Game Over", True, GREEN, BLACK)

    game_score = system_font.render("Scores: " + str(scores), True, GREEN, BLACK)

    # 뱀이 바나나와 충돌하면(먹으면), 스코어 1점 획득
    # 바나나는 오른쪽 화면에서 y좌표 랜덤으로 나타남
    if snake_rect.colliderect(banana_rect):
        scores += 1
        banana_rect.x = WINDOW_WIDTH + 50
        banana_rect.y = random.randint(65, WINDOW_HEIGHT - 32)

    # 움직이기 전에 배경을 검은색으로 채움. (이동한 다음에 남는 이미지를 없애기 위함)
    display_surface.fill((0, 0, 0))

    # 앞에서 검은색으로 채운 다음에 키보드 입력을 해서 바뀐 위치에 이미지를 화면에 붙임.
    display_surface.blit(snake_image, snake_rect) # 이미지를 화면에 붙이는 함수
    display_surface.blit(mouse_image, mouse_rect) # 이미지를 화면에 붙이는 함수
    display_surface.blit(banana_image, banana_rect) # 이미지를 화면에 붙이는 함수

    display_surface.blit(game_live, game_live_rect)
    display_surface.blit(game_score, game_score_rect)

    # 디스플레이 업데이트 (이게 없으면 위에 있는 코드들이 게임에 업데이트 되지 않아서 적용되지 않음)
    pygame.display.update()

    clock.tick(60) # 게임을 60 프레임으로 만듦

# 게임을 나감
pygame.quit()
