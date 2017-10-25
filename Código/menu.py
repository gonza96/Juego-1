import pygame
from main import *

class Menu:
	def __init__(self, opciones):
		self.opciones = opciones
		self.font = pygame.font.Font("Fuente/PressStart2P-Regular.ttf", 23)
		self.seleccionado = 0
		self.total = len(self.opciones)
		self.mantiene_pulsado = False

	def actualizar(self):
		k = pygame.key.get_pressed()

		if not self.mantiene_pulsado:
			if k[pygame.K_UP]:
				self.seleccionado -= 1
			elif k[pygame.K_DOWN]:
				self.seleccionado += 1
			elif k[pygame.K_RETURN]:

				# Invoca a la función asociada a la opción.
				titulo, funcion = self.opciones[self.seleccionado]
				print("Selecciona la opción '%s'." % titulo)
				funcion()

		# Procura que el cursor esté entre las opciones permitidas
		if self.seleccionado < 0:
			self.seleccionado = 0
		elif self.seleccionado > self.total - 1:
			self.seleccionado = self.total - 1

		# Indica si el usuario mantiene pulsada alguna tecla.
		self.mantiene_pulsado = k[pygame.K_UP] or k[pygame.K_DOWN] or k[pygame.K_RETURN]

	def imprimir(self, pantalla):
		total = self.total
		indice = 0
		altura_de_opcion = 35
		x = pantalla.get_width() / 2 - 120
		y = pantalla.get_height() / 2 - 100

		for (titulo, funcion) in self.opciones:
			if indice == self.seleccionado:
				color = (ROJO)
			else:
				color = (BLANCO)

			imagen = self.font.render(titulo, 1, color)
			posicion = (x, y + altura_de_opcion * indice)
			indice += 1
			pantalla.blit(imagen, posicion)

def comenzar_nuevo_juego():
	nombre = ""
	jugar(cant_alien, nombre)

def cargar_partida():
	pass

def como_jugar():

	volver = False

	while not volver:

		teclas = pygame.key.get_pressed()

		for evento in pygame.event.get():
			if evento.type == pygame.QUIT or teclas[pygame.K_q]: volver = True

		pantalla.blit(fondo_teclas, (0, 0))

		pygame.display.flip()
		pygame.time.delay(10)

def creditos():

	volver = False

	while not volver:

		teclas = pygame.key.get_pressed()

		for evento in pygame.event.get():
			if evento.type == pygame.QUIT or teclas[pygame.K_q]:
				volver = True

		pantalla.blit(fondo_creditos, (0, 0))

		pygame.display.flip()
		pygame.time.delay(10)

def salir_del_programa():
	import sys
	print ("Gracias por utilizar este programa.")
	pygame.quit()
	sys.exit(0)

if __name__ == '__main__':

	salir = False
	iniciado = False

	opciones = [
		("Nuevo juego", comenzar_nuevo_juego),
		("Cómo jugar", como_jugar),
		("Creditos", creditos),
		("Salir", salir_del_programa)
		]

	menu = Menu(opciones)

	while not salir:
		teclado = pygame.key.get_pressed()
		for e in pygame.event.get():
			if e.type == pygame.QUIT or teclado[pygame.K_q]:
				salir_del_programa()

		pantalla.blit(imagen_fondo, (0, 0))

		menu.actualizar()
		menu.imprimir(pantalla)

		pygame.display.flip()
		pygame.time.delay(10)
