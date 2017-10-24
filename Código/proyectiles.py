import pygame

lista_proyectil = []
velocidad_proyectil = 10
# Definición de la clase proyectiles
class Proyectiles(pygame.sprite.Sprite):
	

	def __init__(self, image, velocidad_proyectil):
		super().__init__()
		self.image = image
		self.rect = self.image.get_rect()
		

	# Desplaza los proyectiles hacia arriba de la pantalla
	def mover_proyectil(self, largo_lista_proy):
		if largo_lista_proy > 0:
			for i in range(largo_lista_proy):
				if lista_proyectil[i][1] > 0:
				

					lista_proyectil[i][1] -= velocidad_proyectil
					if lista_proyectil[i][1] <= 0:
						del lista_proyectil[i]
						break
					
	# Añade un nuevo proyectil a la lista	   

	# Añade un nuevo proyectil a la lista
	def nuevo_disparo(self, jugador_x, jugador_y):
		lista_proyectil.append([jugador_x, jugador_y])
