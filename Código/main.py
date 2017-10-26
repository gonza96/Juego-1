import pygame
from jugador import *
from estrellas import *
from proyectiles import *
from aliens import *

pygame.init()

# Definición de colores, fuentes de texto y variables globales
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
AZUL = (0, 250, 255)

# Pantalla
pantalla = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Developer Vs. Java")
pygame.mouse.set_visible(0)

# Fuentes
fuente = pygame.font.Font("Fuente/PressStart2P-Regular.ttf", 36)
fuente2 = pygame.font.Font("Fuente/PressStart2P-Regular.ttf", 12)
fuente3 = pygame.font.Font("Fuente/PressStart2P-Regular.ttf", 35)

reloj = pygame.time.Clock()
hecho = False
vel_x = 0
vel_y = 0

velocidad = 3

# Imágenes
imagen_fondo = pygame.image.load("Imagenes/Fondo/fondo_menu.png")
fondo_creditos = pygame.image.load("Imagenes/Fondo/fondo_creditos.png")
fondo_teclas = pygame.image.load("Imagenes/Fondo/fondo_teclas.png")
fondo_juego = pygame.image.load("Imagenes/Fondo/fondo_juego.png")
fondo_historia = pygame.image.load("Imagenes/Fondo/fondo_historia.png")

imagen_jugador = pygame.image.load("Imagenes/Jugador/player_R1.png")
imagen_jugador.set_colorkey(BLANCO)

imagen_proyectil = pygame.image.load("Imagenes/Jugador/hand.png")
imagen_proyectil.set_colorkey(BLANCO)

imagen_alien = pygame.image.load("Imagenes/Café/cup.png")
cant_alien = 73
ancho_imagen = imagen_alien.get_width()
rect_alien = imagen_alien.get_rect()

imagen_bed = pygame.image.load("Imagenes/Obstaculos/bed.png")
imagen_bed.set_colorkey(BLANCO)

imagen_dog = pygame.image.load("Imagenes/Obstaculos/dog.png")

imagen_clock = pygame.image.load("Imagenes/Obstaculos/clock.png")

# Sonidos
pygame.mixer.music.load("Sonidos/musica_juego.wav")
sonido_disparo = pygame.mixer.Sound("Sonidos/sonido_disparo.wav")

# Inicializa Jugador, estrellas, aliens y proyectiles
estrellas = Estrellas(pantalla)
jugador1 = Jugador(imagen_jugador, velocidad, pantalla, 0)
proyectiles = Proyectiles(imagen_proyectil, velocidad_proyectil)
iniciar_aliens(cant_alien)
pygame.mixer.music.play(10)

# Bucle principal del juego
def jugar(cant_alien, nombre):

	hecho = False
	ciclos = 0
	cantMov = 0
	cont = 0
	cant_alien_visible1 = 0
	cant_alien_visible2 = 0

	obstaculos(imagen_bed, pantalla)

	#obstaculos(imagen_dog, pantalla)

	obstaculos(imagen_clock, pantalla)

	while not hecho:

		# Borra la pantalla
		pantalla.fill(NEGRO)
		pantalla.blit(fondo_juego, (0, 0))

		# Busca teclas presionadas
		teclas = pygame.key.get_pressed()
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT or teclas[pygame.K_q]:
				hecho = True
			if evento.type == pygame.MOUSEBUTTONDOWN or teclas[pygame.K_f]:
				sonido_disparo.play()
				pos_disparo = (jugador1.rect.x + (jugador1.image.get_width() / 2) - (proyectiles.image.get_width() / 2))
				proyectiles.nuevo_disparo(pos_disparo, jugador1.rect.y)

		# Dibuja en pantalla los proyectiles disparados
		if len(lista_proyectil) != 0:
			for i in range(len(lista_proyectil)):
				pantalla.blit(imagen_proyectil, lista_proyectil[i])

		# Dibuja en pantalla los aliens
		if len(lista_alien) != 0:
			for i in range(len(lista_alien)):
				pantalla.blit(imagen_alien, lista_alien[i])

		# Dibuja los obstáculos en pantalla
		if len(lista_obstaculos) != 0:
			for i in range(len(lista_obstaculos)):
				pantalla.blit(imagen_bed, (lista_obstaculos[i][0], lista_obstaculos[i][1]))

		#if len(lista_obstaculos) != 0:
		#	for i in range(len(lista_obstaculos)):
		#		pantalla.blit(imagen_dog, (lista_obstaculos[i][0], lista_obstaculos[i][1]))

		if len(lista_obstaculos) != 0:
			for i in range(len(lista_obstaculos)):
				pantalla.blit(imagen_clock, (lista_obstaculos[i][1], lista_obstaculos[i][0]))

		# Llamado a la función de colisiones, verifica cantidad de aliens en pantalla
		# para ver si alguno fue eliminado
		cant_alien_visible1 = len(lista_alien)
		Colisiones(lista_alien, lista_proyectil, ancho_imagen)
		cant_alien_visible2 = len(lista_alien)

		# Si se elimino un enemigo, suma 50 puntos
		if(cant_alien_visible2 < cant_alien_visible1):
			jugador1.puntos += 50

		# Actualiza la cantidad de proyectiles
		largo_lista_proy = len(lista_proyectil)

		# Llamado para desplazar los proyectiles y las estrellas
		estrellas.actualizar_pos(lista_estrella, pantalla)
		proyectiles.mover_proyectil(largo_lista_proy)

		# Actualiza posicion obstaculos
		mover_obstaculos(imagen_bed, pantalla)

		#mover_obstaculos(imagen_dog, pantalla)

		mover_obstaculos(imagen_clock, pantalla)

		# Si se destruyen todos los aliens agrega más
		if len(lista_alien) == 0:
			#if cant_alien < 127:
			#	cant_alien += 18
			iniciar_aliens(cant_alien)

		# Llamado a la función para mover los aliens
		if ciclos == 0:
			mover_alien(lista_alien, ciclos, pantalla)
			cantMov += 1
			if cantMov == 50:
				cantMov = 0
				ciclos = 1

		if ciclos == 1:
			mover_alien(lista_alien, ciclos, pantalla)
			cantMov += 1
			if cantMov == 50:
				cantMov = 0
				ciclos = 0

		cont += 1
		if cont == 120:
			mover_alien_y(lista_alien)
			cont = 0

		# Actualiza la posición x,y del jugador y lo dibuja en pantalla
		jugador1.actualizar_pos(velocidad, teclas, pantalla)
		jugador1.dibujar(pantalla)
		jugador1.colision_alien(lista_alien, pantalla)

		# Colision con obstaculos
		colision_obstaculos(jugador1, imagen_bed, pantalla)

		# Nombre y puntuación en pantalla
		nombre = "Jugador"
		nombre_puntos = fuente2.render(nombre+" Puntos: "+ str(jugador1.puntos), 1, (BLANCO))
		pantalla.blit(nombre_puntos, (0, 0))

		# Imprime en pantalla todos los gráficos
		pygame.display.flip()

		reloj.tick(90)
