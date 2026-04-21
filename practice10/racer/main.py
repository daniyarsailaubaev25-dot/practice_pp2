import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
READ = (255,0,0)

player_width = 50
player_height = 80

player_x = WIDTH // 2
player_y = HEIGHT - 120
player_speed = 10

coins = []
coin_size = 20
coin_spawn_delay = 30
spawn_timer = 0

score = 0

font = pygame.font.Font(None, 36)

def spawn_coin():
    x = random.randint(0, WIDTH - coin_size)
    y = -coin_size
    coins.append(pygame.Rect(x, y, coin_size, coin_size))

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(0, min(WIDTH - player_width, player_x))

    player_rect = pygame.Rect(player_x+60, player_y, player_width, player_height)

    car_img = pygame.image.load("practice_10/racer/image/carr.png")
    car_img = pygame.transform.scale(car_img, (player_width+40, player_height))

    spawn_timer += 1
    if spawn_timer >= coin_spawn_delay:
        spawn_coin()
        spawn_timer = 0

    for coin in coins[:]:
        coin.y += 14

        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 1
        elif coin.y > HEIGHT:
            coins.remove(coin)

    screen.fill(BLACK)

    screen.blit(car_img, (player_x, player_y))

    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin.center, coin_size // 2)

    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 10))

    pygame.display.update()

pygame.quit()
sys.exit()