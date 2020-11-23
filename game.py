import pygame
from player import Player
#from shot import Shot
from enemy import Enemy

class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = []
#        self.pressed = {}
#        self.shot = Shot()

    def generate_enemies(self):
        for i in range(20):
            self.enemies.append(Enemy())