import pygame
import random

# --- Global constants ---
COLOR_FONDO = (227, 158, 193)
COLOR_GUIA = (172, 172, 222)
COLOR_CIRCULO = (184, 51, 106)
NEGRO = (229, 252, 255)
BLACK = (0, 0, 0)
IMAGEN_FONDO = "osu.jpeg"

ANCHO_VENTANA = 700
ALTO_VENTANA = 500

# --- Classes ---

class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """

    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        picture = pygame.image.load("circle.png").convert()
        background_image = pygame.transform.scale(picture, (55, 55))
        self.image = background_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(60, ALTO_VENTANA)
        self.rect.x = random.randrange(-300, -20)

    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.x += 1

        if self.rect.x > ANCHO_VENTANA + self.rect.width:
            self.reset_pos()


class Player(pygame.sprite.Sprite):
    """ This class represents the player. """

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player location. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Game(object):
    song = "Humph! - Pentagon"
    pygame.font.init()
    fuente = pygame.font.Font(None, 20)
    musica_fondo = pygame.mixer
    musica_fondo.init()
    musica_fondo.music.load(
        'C:/Users/Pamela/Documents/GitHub/py-diaz-pachacama-b612/proyecto-osu/recursos/pentagon-humph.ogg')
    musica_fondo.music.play(-1)

    def __init__(self):
        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # BLOQUES
        ypos = (100, 200, 300, 400, 500)
        xpos = [100, 200, 300, 400, 500, 600, 700]
        counter = 0
        for i in range(20):
            block = Block()
            if (counter > 6):
                counter = 0
            else:
                block.rect.x = xpos[counter]
                counter =  counter + 1
            block.rect.y = random.choice(ypos)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # JUGADOR
        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
                else:
                    blocks_hit_list = [s for s in self.block_list if s.rect.collidepoint(pos)]
                    for block in blocks_hit_list:
                        self.score += 1
                        print(self.score)

        return False

    def run_logic(self):
        if not self.game_over:
            self.block_list.update()
            if len(self.block_list) == 0:
                self.game_over = True

        return False


    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(COLOR_FONDO)

        if self.game_over:
            self.musica_fondo.music.stop()
            text = self.fuente.render(F"Perdiste, tu puntuación final es: {self.score}. Haz clic para jugar de nuevo", True,
                                  NEGRO)
            center_x = (ANCHO_VENTANA // 2) - (text.get_width() // 2)
            center_y = (ALTO_VENTANA // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            puntuacion = self.fuente.render(f"Puntuación: {self.score}", True, NEGRO)
            cancion_sonando = self.fuente.render(f"Canción sonando: {self.song}", True, NEGRO)
            screen.blit(puntuacion, (550, 30))
            screen.blit(cancion_sonando, (30, 30))
            self.all_sprites_list.draw(screen)

        pygame.display.flip()

def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
    size = [ANCHO_VENTANA, ALTO_VENTANA]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Juego OSU!")
    pygame.mouse.set_visible(False)

    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # Main game loop
    while not done:
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)

    # Close window and exit
    pygame.quit()


# Call the main function, start up the game
if __name__ == "__main__":
    main()
