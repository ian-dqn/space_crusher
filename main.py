# This will be the game loop.

# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# space images taken from http://www.freepik.com
import pygame
from player import Player
from game import Game

"""

to fill all the screen in white
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

"""


screen = pygame.display.set_mode((640, 480))  # Notice the tuple! It's not 2 arguments.
clock = pygame.time.Clock()
FPS = 20  # This variable will define how many frames we update per second.
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

clock.tick(FPS)
back = pygame.image.load("sprite/space.jpg")

font = pygame.font.SysFont("comicsans", 50)

game = Game()
lives = font.render(f"Lives: {game.player.lives}", 10, (255, 255, 255))
win = font.render("YOU WIN !", 100, (255, 0, 0))
screen.blit(lives, (10, 10))
launch = True
begin = True
while launch:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launch = False
            quit()
    game.player.playerUpdate()
    screen.blit(back, [0, 0])
    if begin == True:
        game.generate_enemies()
    begin = False
    if len(game.enemies) == 0:
        screen.blit(win, (270, 230))
    else:
        for i in game.enemies:
            i.movement()
            if i.collision(game.player.bullet):
                game.enemies.remove(i)
            screen.blit(i.image, i.rect)
    screen.blit(game.player.image, game.player.rect)
    #screen.blit()
    for shot in game.player.bullet:
        screen.blit(shot.image, shot.rect)
        shot.shot_update()
    pygame.display.flip()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
