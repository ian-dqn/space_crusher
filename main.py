# This will be the game loop.

# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# space image taken from http://www.freepik.com
import pygame
from game import Game
from menu import Menu
import utils

#game necesities
screen = pygame.display.set_mode((640, 480))  #Notice the tuple! It's not 2 arguments
clock = pygame.time.Clock()
FPS = 20                                      #This variable will define how many frames we update per second. Old computer so I let it a 20/s
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))
clock.tick(FPS)

#load back image ans font
back = pygame.image.load("sprite/space.jpg")
font = pygame.font.SysFont("comicsans", 50)
screen.blit(back, [0, 0])  # print back image
game = Game(screen)  # init game class

over = font.render("GAME OVER...", True, (255, 0, 0))
begin = True
while 1:
    menu = Menu(screen, game.score)
    launch = menu.main()
    if begin == False:        #reinit game after menu to have score and not welcome message...
        game = Game(screen)  # init game class
    begin = False
    while launch:                               #game loop
        for event in pygame.event.get():        #checkin for click on the red cross to quit
            if event.type == pygame.QUIT:
                launch = False
                quit()
        game.player.player_update()              #function playerUpdate of the class player
        screen.blit(back, [0, 0])               #print back image
        utils.render_font(screen, game.player.lives, game.score)

        if len(game.enemies) == 0:              #no more enemies
            game.generate_enemies()

        for enemy in game.enemies:                  #iterate in list of enemies
            enemy.movement(game.player.rect.x, game.player.rect.y)    #movement function of the enemy class
            if enemy.collision(game.player):
                if game.player.lives <= 0:
                    screen.blit(over, (202, 230))
                    launch = False
                    break
                else: #game.player.lives > 0:
                    game.player.lives -= 1
                    game.enemies.remove(enemy)
                    pygame.time.wait(1200)      #pause of 1.2s
            if enemy.kill(game.player.bullet):
                game.game_update(enemy)
            screen.blit(enemy.image, enemy.rect)                    #print enemies
        screen.blit(game.player.image, game.player.rect)        #print player

        for shot in game.player.bullet:
            screen.blit(shot.image, shot.rect)
            if shot.shot_update():                           #bullets movements, if True rm shot
                game.player.bullet.remove(shot)
        pygame.display.flip()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
