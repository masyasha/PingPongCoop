import pygame
import player_platform
import ball
from pygame import *

WIN_WIDTH = 750
WIN_HEIGHT = 400
WINDOW = (WIN_WIDTH, WIN_HEIGHT)
BG_COLOR = "#ff7f7f"


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW)
    pygame.display.set_caption("Ping Pong Babe")
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BG_COLOR))
    bg = image.load("bg_table.jpg")
    clock = pygame.time.Clock()
    timer = 0
    platforms = []
    objects = pygame.sprite.Group()
    player1 = player_platform.Platform(50, 175)
    player2 = player_platform.Platform(680, 175)
    platforms.append(player1)
    platforms.append(player2)
    objects.add(player1, player2)
    up = down = False

    movingBall = ball.Circle(screen)
    movingBall.start()  # start round with ball movement

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit, 'Quit'

            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_UP:
                up = False

        screen.blit(bg, (0, 0))
        if timer % 1 == 0:
            player1.update(up, down, player1, player2)
            player2.update(up, down, player1, player2)
            timer = 0
        timer += 1
        objects.draw(screen)
        movingBall.update(screen, player1, player2, movingBall)
        pygame.display.update()
        clock.tick(120)


if __name__ == "__main__":
    main()

