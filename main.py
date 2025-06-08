###importing libraries
from libraries_and_settings import (pygame,
                                    sys)
###importing configurations
from libraries_and_settings import (display_surface)

pygame.init()

class Game:
    def __init__(self):
        self.running = True
        self.display_surface = display_surface

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()

            self.display_surface.fill('black')
            pygame.display.update()


        pygame.quit()

if __name__ == '__main__':
    main_game = Game()
    main_game.run()