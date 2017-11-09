import pygame
from main import *
from menu import *
from tazas import *

ROJO = (255, 0, 0)

# Definición de la clase jugador
class Jugador(pygame.sprite.Sprite):

	def __init__(self, velocidad, pantalla, puntos, suenio):
		super().__init__()

		self.imagen1 = pygame.image.load("Imagenes/Jugador/jug_der1.png")
		self.imagen2 = pygame.image.load("Imagenes/Jugador/jug_der2.png")
		self.imagen3 = pygame.image.load("Imagenes/Jugador/jug_der3.png")
		self.imagen4 = pygame.image.load("Imagenes/Jugador/jug_izq1.png")
		self.imagen5 = pygame.image.load("Imagenes/Jugador/jug_izq2.png")
		self.imagen6 = pygame.image.load("Imagenes/Jugador/jug_izq3.png")

		self.imagenes = [[self.imagen1, self.imagen2, self.imagen3], [self.imagen4, self.imagen5, self.imagen6]]
		self.imagen_actual = 0

		self.imagen = self.imagenes[self.imagen_actual][0]

		self.rect = self.imagen.get_rect()
		self.rect.width = self.rect.width - 10
		self.rect.height = self.rect.height - 50
		self.rect.x = pantalla.get_width() / 2 - self.imagen.get_width() / 2
		self.rect.y = pantalla.get_height() - self.imagen.get_height()
		self.velocidad = velocidad
		self.puntos = 0
		self.suenio = 0

		self.movimiento = False
		self.orientacion = 0

		self.t = 0

		self.u = 0

	# Actualiza la posición del jugador
	def actualizar_pos(self, velocidad, teclas, pantalla):
		if self.rect.y >= 350:
			if teclas[pygame.K_UP] or teclas[pygame.K_w]:
				self.rect.y -= self.velocidad
		if self.rect.y <= pantalla.get_height() - self.imagen.get_height():
			if teclas[pygame.K_DOWN]  or teclas[pygame.K_s]:
				self.rect.y += self.velocidad
		if self.rect.x >= 0:
			if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
				self.rect.x -= self.velocidad
				self.orientacion = 1
				self.movimiento = True
		if self.rect.x <= pantalla.get_width() - self.imagen.get_width():
			if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
				self.rect.x += self.velocidad
				self.orientacion = 0
				self.movimiento = True
		if self.movimiento == True:
			self.siguiente_imagen()


	# Imprime en pantalla al jugador
	def dibujar(self, pantalla):
		self.imagen = self.imagenes[self.orientacion][self.imagen_actual]
		pantalla.blit(self.imagen, self.rect)

	# Comprueba si hay colisión entre el jugador y las tazas
	def colision_alien(self, lista_alien, pantalla):
		rect_alien = (0, 0, 0, 0)

		for i in range(len(lista_alien)):
			rect_alien = (lista_alien[i][0], lista_alien[i][1], 32, 32)
			if self.rect.colliderect(rect_alien):
				self.perder(pantalla)

	def suenio(self, accion, pantalla):
		if self.suenio >= 0 and accion == 1:
			suenio += 1
		if self.suenio >= 10:
			perder(pantalla)
			self.suenio = 0
		if self.suenio >= 1 and accion == 0:
			self.suenio -=1

	def perder(self, pantalla):

		nueva_partida = False

		fuente_perder = pygame.font.Font(None, 50)
		texto_perder = fuente_perder.render("Perdiste", 1, (ROJO))
		texto_reiniciar = fuente_perder.render("Pulsa r para volver a iniciar", 1, (ROJO))
		rect_texto_r = texto_reiniciar.get_rect()
		rect_texto_r.centerx = pantalla.get_rect().centerx
		rect_texto_r.centery = 500
		rect_texto = texto_perder.get_rect()
		rect_texto.centerx = pantalla.get_rect().centerx
		rect_texto.centery = pantalla.get_rect().centery

		while not nueva_partida:
			tecla = pygame.key.get_pressed()
			pantalla.blit(self.imagen, self.rect)
			pantalla.blit(texto_perder, rect_texto)
			pantalla.blit(texto_reiniciar, rect_texto_r)
			pygame.display.flip()

			for evento in pygame.event.get():
				if tecla[pygame.K_r]:
					nueva_partida = True
					self.rect.x = pantalla.get_width() / 2 - self.imagen.get_width() / 2
					self.rect.y = pantalla.get_height() - self.imagen.get_height()
					reset_tazas(lista_tazas)
					self.puntos = 0

					nueva_partida = True

				if evento.type == pygame.QUIT or tecla[pygame.K_q]:
					salir_del_programa()


	def siguiente_imagen(self):
		self.u += 1

		if self.u == 6:
			self.imagen_actual += 1
			self.u = 0

		if self.imagen_actual > (len(self.imagenes)):
			self.imagen_actual = 0
