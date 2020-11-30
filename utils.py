import pygame

def render_font(screen, lives, score):
    font = pygame.font.SysFont("comicsans", 25)
    lives = font.render(f"Lives: {lives}", True, (255, 255, 255))
    score = font.render(f"Score: {score}", True, (255, 255, 255))
    x, y = font_pos(lives)
    screen.blit(lives, (10, 10))
    screen.blit(score, (10, 25))

def font_pos(obj):
    x = 320 - obj.get_rect().width // 2
    y = 240 - obj.get_rect().height // 2
    return x, y
def render_lvl(screen, levels):
    font = pygame.font.SysFont("comicsans", 50)
    lvl = font.render(f"level {levels}", True, (255, 255, 255))

    screen.blit(lvl, (font_pos(lvl)))
    pygame.display.flip()
    pygame.time.wait(1500)      #wait 1,5s

def is_positive(n):
    if n >= 0:
        return True
    else:
        return False
def around(n, min, max):
    if is_positive(min) == False:
        min *= -1
    if is_positive(max) == False:
        max *= -1
    return n - min, n + max