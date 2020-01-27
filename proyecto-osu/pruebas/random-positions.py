import numpy as np

ALTO = 500
ANCHO = 700

arreglo_alto = np.random.permutation(np.arange(40, ALTO, 20))
arreglo_ancho = np.arange(0, ANCHO)

print(arreglo_alto,arreglo_ancho)