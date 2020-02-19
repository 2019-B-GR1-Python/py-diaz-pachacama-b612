# Python Guitar Hero
import random
import pygame
from pygame.locals import *

pygame.init()

gfret = (43, 255, 0)
rfret = (255, 0, 12)
yfret = (255, 255, 0)
bfret = (0, 171, 255)
ofret = (255, 84, 0)
blk = (0, 0, 0)
wte = (255, 255, 255)
#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
done = False
xpos = (250, 350, 450, 550, 650)
note_list = []


def drawBoard(screen):
    pygame.draw.polygon(screen, blk, ((200, 900), (700, 900), (700, 0), (200, 0), (200, 900)), 0)
    pygame.draw.polygon(screen, gfret, ((200, 850), (300, 850), (300, 800), (200, 800), (200, 850)), 0)
    pygame.draw.polygon(screen, rfret, ((300, 850), (400, 850), (400, 800), (300, 800), (300, 850)), 0)
    pygame.draw.polygon(screen, yfret, ((400, 850), (500, 850), (500, 800), (400, 800), (400, 850)), 0)
    pygame.draw.polygon(screen, bfret, ((500, 850), (600, 850), (600, 800), (500, 800), (500, 850)), 0)
    pygame.draw.polygon(screen, ofret, ((600, 850), (700, 850), (700, 800), (600, 800), (600, 850)), 0)
    pygame.draw.ellipse(screen, rfret, (100, 100, 90, 50))  # (x,y,stretch x, stretch y


def getFretColor():
    if xpos == 250:
        return (43, 255, 0)
    elif xpos == 350:
        return (255, 0, 12)
    elif xpos == 450:
        return (255, 255, 0)
    elif xpos == 550:
        return (0, 171, 255)
    elif xpos == 650:
        return (255, 84, 0)


pygame.init()
# draws the window
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Python Hero")
screen.fill(wte)
drawBoard(screen)

for i in range(1):
    x = random.choice(xpos)
    y = random.randrange(-500, -300)
    note_list.append([x, y])

clock = pygame.time.Clock()

# MAIN PROGRAM

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    drawBoard(screen)
    for i in range(len(note_list)):

        pygame.draw.circle(screen, gfret, note_list[i], 25)
        # pygame.draw.circle(screen, getFretColor(), note_list[i], 25)

        note_list[i][1] += 3
        pygame.display.flip()
        if note_list[i][1] > 900:
            y = random.randrange(-3000, -300)
            note_list[i][1] = y
            x = random.choice(xpos)
            note_list[i][0] = x

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
