from main import *

lista_alien = []

# Función para mover los aliens en el eje x
def mover_alien(lista_alien, ciclos, pantalla):
						
		if len(lista_alien) > 0:
			for i in range(len(lista_alien)):
				if ciclos == 1:
					if(lista_alien[i][0] > 32):
						lista_alien[i][0] -= 1
					#if(lista_alien[i][0] <= 32):
					#	lista_alien[i][0] += 1000
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

						
						
						
						
						
						
						
						
						
						
						
