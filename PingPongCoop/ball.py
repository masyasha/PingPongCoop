import pygame, random
import player_platform
import math
from pygame import *

WIN_WIDTH = 750
WIN_HEIGHT = 400

CIRCLE_RADIUS = 10
CIRCLE_SIDE = CIRCLE_RADIUS * 2
CIRCLE_X = (WIN_WIDTH / 2)
CIRCLE_Y = (WIN_HEIGHT / 2)
BALL_SPEED = 2
CIRCLE_COLOR = "#ffa500"


class Circle(sprite.Sprite):
    def __init__(self, screen):
        sprite.Sprite.__init__(self)
        self.x = CIRCLE_X
        self.y = CIRCLE_Y
        self.ball = draw.circle(screen, Color(CIRCLE_COLOR), (self.x, self.y), CIRCLE_RADIUS)
        self.x_vel = self.y_vel = 0

    def start(self):
        right = []
        left = []
        for i in range(10):
            ran = random.randint(1, 2)
            if ran == 1:
                right.append(ran)
            elif ran == 2:
                left.append(ran)
        rightSide = True if sum(right) > sum(left) / 2 else False

        if rightSide:
            self.y_vel = random.randint(-BALL_SPEED, BALL_SPEED)
            self.x_vel = BALL_SPEED
        if not rightSide:
            self.x_vel = -BALL_SPEED
            self.y_vel = random.randint(-BALL_SPEED, BALL_SPEED)

        print self.x_vel, self.y_vel

    def update(self, screen, player1, player2, ball):

        self.collide(player1, player2, ball)

        self.x += self.x_vel
        self.y += self.y_vel

        draw.circle(screen, Color(CIRCLE_COLOR), (self.x, self.y), CIRCLE_RADIUS)

    def collide(self, player1, player2, ball):

        if player1.rect.x + player_platform.PLATFORM_WIDTH <= ball.x:
            if ball.y + CIRCLE_RADIUS <= player1.rect.y + player_platform.PLATFORM_HEIGHT and ball.y >= player1.rect.y:
                self.x_vel = -self.x_vel

        if ball.x + CIRCLE_RADIUS <= player2.rect.x:
            if ball.y + CIRCLE_RADIUS <= player2.rect.y + player_platform.PLATFORM_HEIGHT and ball.y >= player2.rect.y:
                self.x_vel = -self.x_vel

        if player1.rect.y + player_platform.PLATFORM_HEIGHT <= ball.y:
            pass

        if ball.x <= 0 or ball.x >= WIN_WIDTH - CIRCLE_RADIUS:  # border collisions
            self.x_vel = -self.x_vel

        if ball.y <= 0 or ball.y >= WIN_HEIGHT - CIRCLE_RADIUS:
            self.y_vel = -self.y_vel
