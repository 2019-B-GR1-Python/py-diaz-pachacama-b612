import numpy as np
import random

ALTO = 500
ANCHO = 700
ypos = (250, 350, 450, 550, 650)
note_list = []
arreglo_alto = np.random.permutation(np.arange(40, ALTO, 20))
arreglo_ancho = np.arange(0, ANCHO)
for i in range(3):
    x = random.choice(xpos)
    y = random.randrange(-500, -300)
    note_list.append([x, y])

print(note_list)
