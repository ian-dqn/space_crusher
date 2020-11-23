import random
import pygame
from player import Player

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.image = pygame.image.load("sprite/basic_enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(2, 638) #generate random pos x in the screen
        self.rect.y = random.randint(2, 300) #generate random pos y in the up screen
        self.mask = pygame.mask.from_surface(self.image)

    def movement(self):
        x = random.randint(0, 4)
        if x == 0 and self.rect.x > 2:
            self.rect.x -= self.speed
        if x == 1 and self.rect.x < 608:
            self.rect.x += self.speed
        if x == 2 and self.rect.y > 2:
            self.rect.y -= self.speed
        if x == 3 and self.rect.y < 470:
            self.rect.y += self.speed

    def collision(self, obj):
        for i in obj:
            if pygame.sprite.collide_mask(self, i):
                return True
        return False