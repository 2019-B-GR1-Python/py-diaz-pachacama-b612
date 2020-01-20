import pygame

pygame.init()
screen = pygame.display.set_mode((1920,1200))
clock = pygame.time.Clock()
pygame.display.set_caption("OSU! Game")
background_image = pygame.image.load("osu.jpeg").convert()

done = False
size = (50, 50)
size_borde = (100,100)
radio = 25
radio_borde = 50
#CONSTANTES
BORDE = 5

# COLORES
COLOR_CIRCULO = pygame.Color(71, 98, 79)
COLOR_BORDE = pygame.Color(82, 173, 156)
COLOR_FONDO = (0, 0, 0)
# FIN COLORES


def dibujar_circulo(tamanio, radio, is_guia = True):
	circle = pygame.Surface(tamanio)	
	if(is_guia):
		pygame.draw.circle(circle, COLOR_BORDE, (radio, radio), radio, BORDE)
	else:
		pygame.draw.circle(circle, COLOR_CIRCULO, (radio, radio), radio)
	return circle

# CIRCULOS
circle_filled = dibujar_circulo(size, radio, False)
circle = dibujar_circulo(size_borde,radio_borde)
# FIN CIRCULOS

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	# Visible o no el cursor
	screen.blit(background_image, [0, 0])
	pygame.mouse.set_visible(True)
	x, y = pygame.mouse.get_pos()
	screen.blit(circle_filled, (x, y))
	pygame.display.flip()
	clock.tick(60)


	
	
