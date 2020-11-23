import pygame
from pygame.locals import *

from shot import Shot

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.attack = 10
        self.speed = 10
        self.image = pygame.image.load("spaceships/png/attack-plane-4.png")
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 440
        self.mask = pygame.mask.from_surface(self.image)
        self.bullet = []#pygame.sprite.Group()

    def playerUpdate(self):
        key = pygame.key.get_pressed()
        if key[K_SPACE]:
            self.bullet.append(Shot(self.rect.x, self.rect.y))
            #print(self.bullet[0])
        if key[K_RIGHT] and self.rect.x < 608:# - self.player.get_width():
            self.rect.x += self.speed
        elif key[K_LEFT] and self.rect.x > 2:
            self.rect.x -= self.speed
        elif key[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed
        elif key[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
"""
    def move_right(self):
        if self.rect.x < 608:
#            self.rect.move(0, 0)#self.rect.x - self.speed, self.rect.y)
            self.rect.x += self.velocity

    def move_left(self):
        if self.rect.x > 2:
            self.rect.x -= self.velocity

    def move_down(self):
        if self.rect.y < 445:
            self.rect.y += self.velocity

    def move_up(self):
        if self.rect.y > 10:
            self.rect.y -= self.velocity"""