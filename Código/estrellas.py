import pygame
import random
from main import *

pygame.font.init()
fuente = pygame.font.Font("Fuente/PressStart2P-Regular.ttf", 12)

BLANCO = (255, 255, 255)
lista_estrella = []

# Definición de la clase estrellas
class Estrellas(pygame.sprite.Sprite):

	def __init__(self, pantalla):

		# Genera 100 estrellas en posiciones aleatorias
		for i in range(100):
			self.estrella_x = random.randrange(0, pantalla.get_width())
			self.estrella_y = random.randrange(0, pantalla.get_height())
			self.estrella_z = random.randrange(0, 2)
			lista_estrella.append([self.estrella_x, self.estrella_y, self.estrella_z])

	def actualizar_pos(self, lista_estrella, pantalla):
				
		# Desplaza las estrellas una posición hacia abajo
		for i in range(len(lista_estrella)):
			x, y = lista_estrella[i][0], lista_estrella[i][1]
			#pygame.draw.circle(pantalla, BLANCO, lista_estrella[i], 2)
			binario = fuente.render(str(lista_estrella[i][2]), 1, (BLANCO))
			pantalla.blit(binario, (x, y))
			#print(lista_estrella[i][2])
			
			lista_estrella[i][1] += 1
			# Si la estrella sale de la pantalla asigna una nueva posición

			if lista_estrella[i][1] > pantalla.get_height():
				y = random.randrange(-50, -10)
				lista_estrella[i][1] = y
				x = random.randrange(0, pantalla.get_width())
				lista_estrella[i][0] = x
