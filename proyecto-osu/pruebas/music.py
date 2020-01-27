import pygame

pygame.mixer.init()
pygame.mixer.music.load("/home/dev-05/Documents/ld-python/py-diaz-pachacama-b612/proyecto-osu/pentagon-humph.ogg")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	pass