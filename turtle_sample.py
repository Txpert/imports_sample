import pygame
import sys

# Initialisiere Pygame
pygame.init()

# Bildschirmgröße
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Farben
black = (0, 0, 0)
white = (255, 255, 255)

# Ball Eigenschaften
ball_size = 20
ball_speed_x = 5
ball_speed_y = 5
ball = pygame.Rect(screen_width / 2 - ball_size / 2, screen_height / 2 - ball_size / 2, ball_size, ball_size)

# Spieler Schläger Eigenschaften
paddle_width = 10
paddle_height = 100
player_speed = 10
player1 = pygame.Rect(10, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)
player2 = pygame.Rect(screen_width - 20, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)

# Spiel Schleife
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tastendrücke erfassen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < screen_height:
        player1.y += player_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < screen_height:
        player2.y += player_speed

    # Ball Bewegung
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball Kollision mit Wänden
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    # Ball Kollision mit Schlägern
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Bildschirm aktualisieren
    screen.fill(black)
    pygame.draw.rect(screen, white, player1)
    pygame.draw.rect(screen, white, player2)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.flip()
    clock.tick(60)
