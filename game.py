import pygame
from player import Player
from enemy import Enemy
from utils import render_lvl
from explosion_animation import Animation

class Game:
    """
        main game class
    """
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.enemies = []
        self.explosion = Animation()
        self.score = 0
        self.level = 1
        self.levels = [0, 50, 100, 300, 500, 700, 1000, 1300, 1600, 2000]

    def game_update(self, enemy):
        if enemy in self.enemies:
            self.display_explosion(enemy)
            self.enemies.remove(enemy)
            self.score += 10

        if self.score in self.levels:
            self.level = self.levels.index(self.score) + 1
            render_lvl(self.screen, self.level)             #from utils.py
            self.player.lives += 1

    def generate_enemies(self):
        if self.level == 10:
            self.level = 20
        for i in range(self.level * 2):
            self.enemies.append(Enemy(self.player.rect.y))

    def display_explosion(self, enemy):
        for i in range(len(self.explosion.explosion_lst)):
            self.screen.blit(self.explosion.explosion_lst[i], (enemy.rect.x, enemy.rect.y))
            pygame.time.wait(15)
