import random
import pygame
from player import Player
from utils import is_positive, around

class Enemy(pygame.sprite.Sprite):
    """
        Enemy classe,
        Random init of position
        Note that it needs x's and y's player position to not init too close of player
    """
    def __init__(self, player_y):
        super().__init__()
        self.speed = random.randint(2, 8)
        self.image = pygame.image.load("sprite/basic_enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(2, 638)            #select randomly a pos for x
        self.rect.y = self.init_pos_y(player_y)         #select randomly a pos for y, not too close of player
        self.mask = pygame.mask.from_surface(self.image)


    def init_pos_y(self, player_y):
        """
            function to init position y of enemies in the screen, but not too close of the player
        """
        #p = Player()
        min, max = around(player_y, -50, 50)
        no = [i for i in range(min, max + 1)]       #zone around the player

        y = [i for i in range(2, 470) if i not in no]
        return random.choice(y)

    def go_to_player(self, dif_x, dif_y):
        """
            determine where do we have to go to follow the player
        """
        if is_positive(dif_x):
            self.rect.x += self.speed // 2   #go right
        else:
            self.rect.x -= self.speed // 2   #go left

        if is_positive(dif_y):
            self.rect.y += self.speed // 2   #go down
        else:
            self.rect.y -= self.speed // 2   #go up


    def dodge(self, dif_x, dif_y):
        """
            trying to dodge player shots
        """
        if is_positive(dif_x):                 #enemy at the left of the player
            self.rect.x -= self.speed                  #go left to try to dodge bullets
        else:
            self.rect.x += self.speed

    def movement(self, player_x, player_y):
        """
            function to estimate moves of enemies.
        """
        close = [i for i in range(-40, 41)]
        dif_x = player_x - self.rect.x
        dif_y = player_y - self.rect.y

        if dif_x in close and dif_y not in close and is_positive(dif_y): #enemy in "danger zone"
            self.dodge(dif_x, dif_y)
        else:
            self.go_to_player(dif_x, dif_y)

    def kill(self, bullets):
        """
            estimate if bullets touch enemies
        """
        i = 0
        for shot in bullets:
            if pygame.sprite.collide_mask(self, shot):
                bullets.remove(shot)
                return True
            i += 1
        return False
    def collision(self, player):
        """
            estimate if enemies touch player
        """
        return pygame.sprite.collide_mask(self, player)