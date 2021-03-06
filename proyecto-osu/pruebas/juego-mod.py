"""
Show the proper way to organize a game using the a game class.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/O4Y5KrNgP_c
"""

import pygame
import random

# --- Global constants ---
COLOR_FONDO = (227, 158, 193)
COLOR_GUIA = (172, 172, 222)
COLOR_CIRCULO = (184, 51, 106)
NEGRO = (229, 252, 255)
IMAGEN_FONDO = "osu.jpeg"


ANCHO_VENTANA = 700
ALTO_VENTANA = 500


# --- Classes ---


class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """

    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(COLOR_CIRCULO)
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
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
    song = "Track 1 - Artista Desconocido"
    pygame.font.init()
    fuente = pygame.font.Font(None, 20)

    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """

        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the block sprites
        for i in range(20):
            block = Block()

            block.rect.x = random.randrange(ANCHO_VENTANA)
            block.rect.y = random.randrange(60, ALTO_VENTANA-20)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # Create the player
        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            # Check the list of collisions.
            for block in blocks_hit_list:
                self.score += 1
                print(self.score)
                # You can do something with "block" here.

            if len(self.block_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(COLOR_FONDO)

        if self.game_over:
            text = self.fuente.render(F"Perdiste, tu puntuación final es: {self.score}. Haz clic para jugar de nuevo", True, NEGRO)
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