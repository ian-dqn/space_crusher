import pygame

class Shot(pygame.sprite.Sprite):
    """
        shot class for the player
    """
    def __init__(self, origin_x, origin_y):
        super().__init__()
        self.image = pygame.image.load("sprite/laser_shot.png")
        self.rect = self.image.get_rect()
        self.rect.x = origin_x
        self.rect.y = origin_y
        self.mask = pygame.mask.from_surface(self.image)

    def shot_update(self):
        self.rect.y -= 20
        if self.rect.y <= 0:
            return True
        else:
            return False