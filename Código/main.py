#
#
#

import pygame
import random
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

pantalla = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Algo del espacio")
pygame.mouse.set_visible(0)
fuente = pygame.font.Font(None, 36)
fuente2 = pygame.font.Font(None, 20)
fuente3 = pygame.font.Font(None, 35)

sonido_click = pygame.mixer.Sound("Sonidos/laser5.ogg")

reloj = pygame.time.Clock()
hecho = False
vel_x = 0
vel_y = 0

velocidad = 3

imagen_fondo = pygame.image.load("Imagenes/FondoNegro.png")

imagen_jugador = pygame.image.load("Imagenes/nave2.png")
imagen_jugador.set_colorkey(BLANCO)

imagen_proyectil = pygame.image.load("Imagenes/explosion5.png")
imagen_proyectil.set_colorkey(BLANCO)

imagen_alien = pygame.image.load("imagenes/alien.png")
cant_alien = 73
ancho_imagen = imagen_alien.get_width()
rect_alien = imagen_alien.get_rect()

# Inicializa Jugador, estrellas, aliens y proyectiles
estrellas = Estrellas(pantalla)
jugador1 = Jugador(imagen_jugador, velocidad, pantalla)
proyectiles = Proyectiles(imagen_proyectil, velocidad_proyectil)
iniciar_aliens(cant_alien)

    
# Bucle principal del juego
def jugar(cant_alien, nombre):

    hecho = False
    ciclos = 0
    cantMov = 0
    puntos = 0
    cont = 0
    
    while not hecho:

        # Borra la pantalla
        pantalla.fill(NEGRO)
        
        # Busca teclas presionadas
        teclas = pygame.key.get_pressed()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or teclas[pygame.K_q]:
                hecho = True
            
            if evento.type == pygame.MOUSEBUTTONDOWN or teclas[pygame.K_f]:
                #sonido_click.play()
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

        # Llamado a la función de colisiones
        Colisiones(lista_alien, lista_proyectil, ancho_imagen, puntos)

        # Actualiza la cantidad de proyectiles
        largo_lista_proy = len(lista_proyectil)

        # Llamado para desplazar los proyectiles y las estrellas
        estrellas.actualizar_pos(lista_estrella, pantalla)
        proyectiles.mover_proyectil(largo_lista_proy)

        # Si se destruyen todos los aliens agrega más
        if len(lista_alien) == 0:
            cant_alien += 18
            iniciar_aliens(cant_alien)

        # Llamado a la función para mover los aliens   
        if ciclos == 0:
            mover_alien(lista_alien, ciclos)
            cantMov += 1
            if cantMov == 50:
                cantMov = 0
                ciclos = 1

        if ciclos == 1:
            mover_alien(lista_alien, ciclos)
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

        # Nombre y puntuación en pantalla
        if(puntos != 0): print(puntos)
        nombre = "Jugador"
        nombre_puntos = fuente2.render(nombre+" Puntos: "+ str(puntos), 1, (BLANCO))
        pantalla.blit(nombre_puntos, (0, 0))
        
        # Imprime en pantalla todos los gráficos
        pygame.display.flip()

        reloj.tick(90)
