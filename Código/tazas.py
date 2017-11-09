from main import *
import pygame
import random

lista_tazas = []
lista_obstaculos = []

ROJO = (255, 0, 0)

# Función para mover las tazas en el eje x
def mover_alien(lista_tazas, ciclos, pantalla):

	if len(lista_tazas) > 0:
		for i in range(len(lista_tazas)):
			if ciclos == 1:
				if(lista_tazas[i][0] > 32):
					lista_tazas[i][0] -= 1
			if ciclos == 0:
				if(lista_tazas[i][0] < pantalla.get_width() - 32):
					lista_tazas[i][0] += 1
				if(lista_tazas[i][0] >= pantalla.get_width() - 32):
					lista_tazas[i][0] = 0


# Función para mover las tazas hacia el jugador
def mover_alien_y(lista_tazas):
	if len(lista_tazas) > 0:
		for i in range(len(lista_tazas)):
			lista_tazas[i][1] += 3

# Coprueba si hay colisiones entre los proyectiles y las tazas
def Colisiones(lista_tazas, lista_proyectil, ancho_imagen):

	borro = False

	if len(lista_tazas) != 0 and len(lista_proyectil) != 0:
		for i in range (len(lista_tazas)):
			s = 0
			while s < ancho_imagen and not borro:
				for j in range (len(lista_proyectil)):
					if lista_tazas[i][0] + s == lista_proyectil[j][0] and lista_proyectil[j][1] <= lista_tazas[i][1] :
						del lista_tazas[i]
						del lista_proyectil[j]
						borro = True
						break
					s = s + 0.25

# Coloca las posiciones x,y de las tazas
def iniciar_tazas(cant_alien):
	s = 0
	cont = 0
	y = 25
	for i in range(cant_alien):
		alien_x = s * 40 + 35
		alien_y = y
		if cont == 18:
			s = 0
			cont = 0
			y += 35
		if cont!= 0:
			s += 1
		cont += 1
		lista_tazas.append([alien_x, alien_y])

# Resetea la lista de las tazas
def reset_tazas(lista_tazas):
	s = 0
	cont = 0
	y = 25

	if(len(lista_tazas)!=73):
	# Completa la lista de tazas
		for i in range(73 - len(lista_tazas)):
			lista_tazas.append([0, 0])

	# Posiciona las tazas
	for i in range(73):
		alien_x = s * 40 + 35
		alien_y = y
		if cont == 18:
			s = 0
			cont = 0
			y += 35
		if cont!= 0:
			s += 1
		cont += 1
		lista_tazas[i] = ([alien_x, alien_y])

# Genera mas "enemigos"

def obstaculos(imagen, pantalla):
	x = 0
	y = pantalla.get_height() - imagen.get_height()
	velocidad = random.randrange(2, 3)
	direccion = random.randrange(0, 2)

	if(len(lista_obstaculos) < 3):
		lista_obstaculos.append([x, y, velocidad, direccion])


def mover_obstaculos(imagen, pantalla):

	if len(lista_obstaculos) != 0:
		for i in range(len(lista_obstaculos)):

			if lista_obstaculos[i][0] < (pantalla.get_width() - imagen.get_width()) and lista_obstaculos[i][3] == 0:
				lista_obstaculos[i][0] += lista_obstaculos[i][2]
			if lista_obstaculos[i][0] >= pantalla.get_width() - imagen.get_width():
				lista_obstaculos[i][3] = 1

			if lista_obstaculos[i][0] > 0 and lista_obstaculos[i][3] == 1:
				lista_obstaculos[i][0] -= lista_obstaculos[i][2]
			if lista_obstaculos[i][0] <= 0:
				lista_obstaculos[i][3] = 0


def reset_obstaculos(lista_obstaculos):
	if len(lista_obstaculos)!= 0:
		for i in range(len(lista_obstaculos)):
			lista_obstaculos[i][0] = random.randrange(0, 500)
			lista_obstaculos[i][2] = random.randrange(2, 5)
			lista_obstaculos[i][3] = random.randrange(0, 2)


def colision_obstaculos(jugador, imagen, pantalla):

	if len(lista_obstaculos) != 0:
		rect_jugador = jugador.rect

		ancho_obstaculo = imagen.get_width()
		alto_obstaculo = imagen.get_height()
		rect_obstaculo = (0, 0, alto_obstaculo, ancho_obstaculo)

		for i in range(len(lista_obstaculos)):
			rect_obstaculo = (lista_obstaculos[i][0], lista_obstaculos[i][1], alto_obstaculo, ancho_obstaculo)
			if jugador.rect.colliderect(rect_obstaculo):
				jugador.perder(pantalla)

				jugador.rect.x = pantalla.get_width() / 2 - jugador.imagen.get_width() / 2
				jugador.rect.y = pantalla.get_height() - jugador.imagen.get_height()
				reset_tazas(lista_tazas)
				reset_obstaculos(lista_obstaculos)
				jugador.puntos = 0



#################################################


class Obstaculo(pygame.sprite.Sprite):

	def __init__(self, pantalla):
		super().__init__()

		self.imagen1 = pygame.image.load("Imagenes/Obstaculos/gato_d1.png")
		self.imagen2 = pygame.image.load("Imagenes/Obstaculos/gato_d2.png")
		self.imagen3 = pygame.image.load("Imagenes/Obstaculos/gato_d3.png")
		self.imagen4 = pygame.image.load("Imagenes/Obstaculos/gato_i1.png")
		self.imagen5 = pygame.image.load("Imagenes/Obstaculos/gato_i2.png")
		self.imagen6 = pygame.image.load("Imagenes/Obstaculos/gato_i3.png")

		self.imagenes = [[self.imagen1, self.imagen2, self.imagen3], [self.imagen4, self.imagen5, self.imagen6]]
		self.imagen_actual = 0

		self.imagen = self.imagenes[self.imagen_actual][0]

		self.rect = self.imagen.get_rect()
		self.rect.x = 0
		self.rect.y = 400
		self.velocidad = random.randrange(1, 3)

		self.movimiento = False
		self.orientacion = 0

		self.t = 0

		self.u = 0

	# Actualiza la posición
	def actualizar_pos(self, pantalla):

		if self.rect.x < (pantalla.get_width() - self.imagen.get_width()) and self.t == 0:
			self.rect.x += self.velocidad
		if self.rect.x >= pantalla.get_width() - self.imagen.get_width():
			self.t = 1
			self.orientacion = 1

		if self.rect.x > 0 and self.t == 1:
			self.rect.x -= self.velocidad
		if self.rect.x <= 0:
			self.t = 0
			self.orientacion = 0

		self.siguiente_imagen()



	# Imprime en pantalla la imagen
	def dibujar(self, pantalla):
		self.imagen = self.imagenes[self.orientacion][self.imagen_actual]
		pantalla.blit(self.imagen, self.rect)

	def siguiente_imagen(self):
		self.u += 1

		if self.u == 6:
			self.imagen_actual += 1
			self.u = 0

		if self.imagen_actual > (len(self.imagenes)):
			self.imagen_actual = 0
			
	def colision(self, jugador, pantalla):
		if self.rect.colliderect(jugador):
			jugador.perder(pantalla)
