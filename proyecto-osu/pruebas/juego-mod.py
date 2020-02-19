import pygame
import random

# --- Global constants ---
COLOR_FONDO = (227, 158, 193)
COLOR_TEXTO = (229, 252, 255)
NEGRO = (0, 0, 0)
IMAGEN_FONDO = "osu.jpeg"
IMAGEN_PUNTERO = "L:/Familia/Documents/2019B-OCTAVOSEMESTRE/Python/py-diaz-pachacama-b612/proyecto-osu/pruebas/puntero.png"
ANCHO_VENTANA = 700
ALTO_VENTANA = 500
CLIC_SEGUNDOS = 1
YPOS = (100, 150, 200, 250, 300, 350, 400)
XPOS = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
PATH_CANCION = "L:/Familia/Documents/2019B-OCTAVOSEMESTRE/Python/py-diaz-pachacama-b612/proyecto-osu/recursos/pentagon-humph.ogg"

# ---- ID PARA API ----

id_usuario = 1
id_cancion = 1

# --- Classes ---

class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
    isClicked = False
    counter = CLIC_SEGUNDOS

    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        picture = pygame.image.load("circle.png").convert()
        background_image = pygame.transform.scale(picture, (55, 55))
        self.image = background_image
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        if (self.isClicked):
            self.isClicked = False
            self.counter = CLIC_SEGUNDOS
            self.rect.x = random.choice(XPOS)
            self.rect.y = random.choice(YPOS)
            return False
        else:
            return True

    def comprobar_tiempo(self):
        if not self.isClicked:
            self.counter -= 1
        else:
            self.counter = CLIC_SEGUNDOS

    def update(self):
        pass


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        picture = pygame.image.load("puntero.png").convert()
        background_image = pygame.transform.scale(picture, (40, 40))
        self.image = background_image
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        # self.image = pygame.Surface([20, 20])
        # self.image.fill(COLOR_TEXTO)
        # self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Game(object):
    song = "Humph! - Pentagon"
    pygame.font.init()
    fuente = pygame.font.Font(None, 20)
    musica_fondo = pygame.mixer
    musica_fondo.init()
    # musica_fondo.music.load(
    #    'C:/Users/Pamela/Documents/GitHub/py-diaz-pachacama-b612/proyecto-osu/recursos/pentagon-humph.ogg')
    musica_fondo.music.load(PATH_CANCION)

    def __init__(self):
        self.musica_fondo.music.play(-1)
        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        bloque = Block()
        bloque.rect.x = int(ANCHO_VENTANA / 2 - 30)
        bloque.rect.y = int(ALTO_VENTANA / 2)

        self.block_list.add(bloque)
        self.all_sprites_list.add(bloque)

        # JUGADOR
        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_over:
                    blocks_hit_list = [s for s in self.block_list if s.rect.collidepoint(pos)]
                    for block in blocks_hit_list:
                        block.isClicked = True
                        self.game_over = block.reset_pos()
                        self.score += 1
                        print(self.score)
            if event.type == pygame.USEREVENT:
                for block in self.block_list:
                    block.comprobar_tiempo()
                    if block.counter < 0:
                        self.game_over = True
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()

            if len(self.block_list) == 0:
                self.game_over = True

        return False

    def display_frame(self, screen):
        screen.fill(COLOR_FONDO)

        if self.game_over:
            self.musica_fondo.music.stop()
            text = self.fuente.render(F"Perdiste, tu puntuación final es: {self.score}. Presiona cualquier tecla para jugar de nuevo",
                                      True,
                                      COLOR_TEXTO)
            center_x = (ANCHO_VENTANA // 2) - (text.get_width() // 2)
            center_y = (ALTO_VENTANA // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            puntuacion = self.fuente.render(f"Puntuación: {self.score}", True, COLOR_TEXTO)
            cancion_sonando = self.fuente.render(f"Canción sonando: {self.song}", True, COLOR_TEXTO)
            nivel_juego = self.fuente.render(f"Nivel Actual: {1}", True, COLOR_TEXTO)
            screen.blit(puntuacion, (550, 30))
            screen.blit(cancion_sonando, (30, 30))
            screen.blit(nivel_juego, (550, 470))
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
    pygame.time.set_timer(pygame.USEREVENT, 1000)

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
