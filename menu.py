import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self, screen, score):
        super().__init__()
        self.screen = screen
        self.score = score

    def main(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # if we click on the red cross to quit
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    return True
                if self.score != 0:
                    self.display_score()
                self.draw()

    def draw(self):
        font = pygame.font.SysFont("comicsans", 50)

        if self.score == 0:
            wlc = font.render("Welcome to", True, (255, 255, 255))
            x = 320 - wlc.get_rect().width // 2
            self.screen.blit(wlc, (x, 80))

        name = font.render("SPACE CRUSHER", True, (255, 255, 255))
        x = 320 - name.get_rect().width // 2
        self.screen.blit(name, (x, 130))

        start = font.render("click to begin adventure", True, (255, 255, 255))
        x = 320 - start.get_rect().width // 2
        self.screen.blit(start, (x, 350))

        pygame.display.flip()

    def display_score(self):
        font = pygame.font.SysFont("comicsans", 50)
        s = font.render(f"Score {self.score}", True, (255, 255, 255))
        x = 320 - s.get_rect().width // 2
        self.screen.blit(s, (x, 270))