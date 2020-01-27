import pygame
import numpy as np

puntuacion = 100
nombre_cancion = "Track 1 - Artista desconocido"
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("OSU! Game")
picture = pygame.image.load("./recursos/osu.jpeg").convert()
background_image = pygame.transform.scale(picture, (600, 400))
done = False
tamanio = (50, 50)
radio = 25
radio_borde = 50

# COLORES
COLOR_CIRCULO = pygame.Color(227, 158, 193)
COLOR_BORDE = pygame.Color(82, 173, 156)
COLOR_NEGRO = pygame.Color(0, 0, 0)

# TEXTO EN PANTALLA
pygame.font.init()
fuente = pygame.font.Font(None, 20)
puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, COLOR_NEGRO)
cancion_sonando = fuente.render(f"Canción sonando: {nombre_cancion}", True, COLOR_NEGRO)

# CONSTANTES
BORDE = 5





# CIRCULOS
# FIN CIRCULOS

def posicion_random():
    posicion_x = np.random.randint(50, 500)
    posicion_y = np.random.randint(300)
    return int(posicion_x), int(posicion_y)

class Circulo:
    radio = None
    tamanio = None
    color = None

    def __init__(self, radio, tamanio, color):
        self.radio = radio
        self.tamanio = tamanio
        self.color = color

    def dibujar_circulo(self, is_guia=False):
            circulo = pygame.Surface(self.tamanio)
            if (is_guia):
                pygame.draw.circle(circulo, self.color, (self.radio, self.radio), self.radio)
            else:
                pygame.draw.circle(circulo, self.color, (self.radio, self.radio), self.radio, BORDE)
            return circulo


posicion = posicion_random()
posicion_1 = posicion_random()
posicion_2 = posicion_random()
contador = 5
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
    screen.blit(background_image, (0, 0))
    screen.blit(puntuacion, (450, 30))
    screen.blit(cancion_sonando, (30, 30))
    # Visible o no el cursor
    # pygame.mouse.set_visible(True)
    # x, y = pygame.mouse.get_pos()
    # circle_filled = dibujar_circulo(tamanio, radio, False)
    # screen.blit(circle_filled, posicion)
    circulo = Circulo(25-contador, (50, 50), COLOR_CIRCULO)
    circulo_guia = Circulo(50, (100, 100), COLOR_BORDE)
    circulo_1 = circulo.dibujar_circulo(True)
    circulo_2 = circulo_guia.dibujar_circulo()
    contador = contador -1
   # screen.blit(circulo_2, posicion)
    screen.blit(circulo_1, posicion)
    screen.blit(circulo_1, posicion_1)
    screen.blit(circulo_1, posicion_2)
    pygame.display.flip()
    clock.tick(60)




