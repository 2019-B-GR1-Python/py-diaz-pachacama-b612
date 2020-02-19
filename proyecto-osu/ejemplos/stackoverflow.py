import pygame
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480))

class Block(object):
    sprite = pygame.image.load("circle.png").convert_alpha()
    def __init__(self, x, y):
        # since x and y will be the mouse position,
        # let x and y be the center of the block
        self.rect = self.sprite.get_rect(centery=y, centerx=x)

blocklist = []

while True:
    # don't forget to clear the screen
    screen.fill((0, 0, 0))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT: exit()
        if event.type == pygame.MOUSEBUTTONUP:
            # get all blocks that "collide" with the current mouse position
            to_remove = [b for b in blocklist if b.rect.collidepoint(mouse_pos)]
            for b in to_remove:
                blocklist.remove(b)

            # if we didn't remove a block, we create a new one
            if not to_remove:
                blocklist.append(Block(*mouse_pos))

    for b in blocklist:
        screen.blit(b.sprite, b.rect)

    pygame.display.update()