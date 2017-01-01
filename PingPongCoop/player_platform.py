from pygame import *
import main

PLATFORM_WIDTH = 20
PLATFORM_HEIGHT = 50
MOVE_SPEED = 3
PLATFORM_COLOR = "#1442e7"


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.y_velocity = 0

    def update(self, up, down, player1, player2):

        if up:
            self.y_velocity = -MOVE_SPEED

        if down:
            self.y_velocity = MOVE_SPEED

        if not (up or down):
            self.y_velocity = 0

        self.rect.y += self.y_velocity
        self.collide(player1, player2)

    def collide(self, player1, player2):
        if sprite.collide_rect(self, player1):

            if player1.rect.y <= 0:
                    self.rect.top = 0

            if player1.rect.y + PLATFORM_HEIGHT >= main.WIN_HEIGHT:
                self.rect.top = main.WIN_HEIGHT - PLATFORM_HEIGHT

        if sprite.collide_rect(self, player2):

            if player2.rect.y <= 0:
                    self.rect.top = 0

            if player2.rect.y + PLATFORM_HEIGHT >= main.WIN_HEIGHT:
                self.rect.top = main.WIN_HEIGHT - PLATFORM_HEIGHT

