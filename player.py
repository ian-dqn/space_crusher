import pygame
from pygame.locals import *

from shot import Shot

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.lives = 5
        self.attack = 10
        self.speed = 10
        self.image = pygame.image.load("sprite/attack-plane-4.png")
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 440
        self.mask = pygame.mask.from_surface(self.image)
        self.bullet = []

    def player_update(self):
        """check keyboards arrow and move the player"""
        key = pygame.key.get_pressed()
        if key[K_SPACE] and len(self.bullet) < 12:
            self.bullet.append(Shot(self.rect.x, self.rect.y))
        if key[K_RIGHT] and self.rect.x < 608:
            self.rect.x += self.speed
        elif key[K_LEFT] and self.rect.x > 2:
            self.rect.x -= self.speed
        elif key[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed
        elif key[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
