from main import *
import pygame
import random

lista_alien = []
lista_obstaculos = []

ROJO = (255, 0, 0)

# Función para mover los aliens en el eje x
def mover_alien(lista_alien, ciclos, pantalla):

	if len(lista_alien) > 0:
		for i in range(len(lista_alien)):
			if ciclos == 1:
				if(lista_alien[i][0] > 32):
					lista_alien[i][0] -= 1
			if ciclos == 0:
				if(lista_alien[i][0] < pantalla.get_width() - 32):
					lista_alien[i][0] += 1
				if(lista_alien[i][0] >= pantalla.get_width() - 32):
					lista_alien[i][0] = 0


# Función para mover los aliens hacia el jugador
def mover_alien_y(lista_alien):
	if len(lista_alien) > 0:
		for i in range(len(lista_alien)):
			lista_alien[i][1] += 3

# Coprueba si hay colisiones entre los proyectiles y los aliens
def Colisiones(lista_alien, lista_proyectil, ancho_imagen):

	borro = False

	if len(lista_alien) != 0 and len(lista_proyectil) != 0:
		for i in range (len(lista_alien)):
			s = 0
			while s < ancho_imagen and not borro:
				for j in range (len(lista_proyectil)):
					if lista_alien[i][0] + s == lista_proyectil[j][0] and lista_proyectil[j][1] <= lista_alien[i][1] :
						del lista_alien[i]
						del lista_proyectil[j]
						borro = True
						break
					s = s + 0.25

# Coloca las posiciones x,y de los aliens
def iniciar_aliens(cant_alien):
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
		lista_alien.append([alien_x, alien_y])

# Resetea la lista de los aliens
def reset_aliens(lista_alien):
	s = 0
	cont = 0
	y = 25

	if(len(lista_alien)!=73):
	# Completa la lista de aliens
		for i in range(73 - len(lista_alien)):
			lista_alien.append([0, 0])

	# Posiciona los aliens
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
		lista_alien[i] = ([alien_x, alien_y])

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
				reset_aliens(lista_alien)
				reset_obstaculos(lista_obstaculos)
				jugador.puntos = 0