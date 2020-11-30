import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.explosion_lst = self.explosion()

    def explosion(self):
        img = []
        rect = []
        begin = "sprite/explosion/Explosion_"
        ext = ".png"
        for i in range(1, 12):
            img.append(pygame.image.load(begin + str(i) + ext))
        return img