#
#
#

import pygame
import random

pygame.init()

# Definición de colores y variables globales

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
AZUL = (0, 250, 255)

lista_estrella = []
lista_proyectil = []
lista_alien = []

pantalla = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Algo del espacio")
pygame.mouse.set_visible(0)
fuente = pygame.font.Font(None, 36)

sonido_click = pygame.mixer.Sound("Sonidos/laser5.ogg")

reloj = pygame.time.Clock()
hecho = False
vel_x = 0
vel_y = 0

velocidad = 3
velocidad_proyectil = 10

imagen_jugador = pygame.image.load("Imagenes/nave2.png")
imagen_jugador.set_colorkey(BLANCO)

imagen_proyectil = pygame.image.load("Imagenes/explosion5.png")
imagen_proyectil.set_colorkey(BLANCO)

imagen_alien = pygame.image.load("imagenes/alien.png")
cant_alien = 15
ancho_imagen = imagen_alien.get_width()

siguiente = False
cont = 0
ciclos = 0
cantMov = 0
contador2 = 0

# Definicion de clases y funciones

class Jugador(pygame.sprite.Sprite):
    
    def __init__(self, imagen, velocidad):
        super().__init__()
        
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = pantalla.get_width() / 2 - self.image.get_width() / 2
        self.rect.y = pantalla.get_height() - self.image.get_height()
        self.velocidad = velocidad

    # Actualiza la posición del jugador
    def actualizar_pos(self, velocidad, teclas):
        if self.rect.y >= 0:
            if teclas[pygame.K_UP] or teclas[pygame.K_w]:
                self.rect.y -= self.velocidad
        if self.rect.y <= pantalla.get_height() - self.image.get_height():
            if teclas[pygame.K_DOWN]  or teclas[pygame.K_s]:
                self.rect.y += self.velocidad
        if self.rect.x >= 0:
            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                self.rect.x -= self.velocidad
        if self.rect.x <= pantalla.get_width() - self.image.get_width():
            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                self.rect.x += self.velocidad
        
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

class Estrellas(pygame.sprite.Sprite):
    
    def __init__(self, pantalla):

        # Genera 100 estrellas en posiciones aleatorias
        for i in range(100):
            self.estrella_x = random.randrange(0, pantalla.get_width())
            self.estrella_y = random.randrange(0, pantalla.get_height())
            lista_estrella.append([self.estrella_x, self.estrella_y])
            
    def actualizar_pos(self, lista_estrella, pantalla):

        # Desplaza las estrellas una posición hacia abajo
        for i in range(len(lista_estrella)):
            pygame.draw.circle(pantalla, BLANCO, lista_estrella[i], 2)
            lista_estrella[i][1] += 1
            # Si la estrella sale de la pantalla asigna una nueva posición
            if lista_estrella[i][1] > pantalla.get_height():
                y = random.randrange(-50, -10)
                lista_estrella[i][1] = y
                x = random.randrange(0, pantalla.get_width())
                lista_estrella[i][0] = x

                
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
    def nuevo_disparo(self, jugador_x, jugador_y):
        lista_proyectil.append([jugador_x, jugador_y])
        
class Alien(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()

    # Desplaza los aliens hacia la izquierda y hacia la derecha
    def mover_alien(self, lista_alien, ciclos):
            
        if len(lista_alien) > 0:
            for i in range(len(lista_alien)):
                if ciclos == 1:
                    lista_alien[i][0] -= 15
                if ciclos == 0:
                    lista_alien[i][0] += 15
                    
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
def iniciar_aliens():
    s = 0
    cont = 0
    y = 25
    if siguiente:
        y += 35
    for i in range(cant_alien):
        alien_x = s * 100 +35
        alien_y = y
        if cont == 7:
            s = 0
            cont = 0
            y +=35
        if cont!= 0:
            s += 1
        cont += 1
        lista_alien.append([alien_x, alien_y])
    #print(len(lista_alien))

# Inicializa Jugador, estrellas, aliens y proyectiles
estrellas = Estrellas(pantalla)
jugador1 = Jugador(imagen_jugador, velocidad)
proyectiles = Proyectiles(imagen_proyectil, velocidad_proyectil)
iniciar_aliens()
otra_variable = Alien(imagen_alien)

# Bucle principal del juego
while not hecho:

    # Borra la pantalla
    pantalla.fill(NEGRO)
    
    # Busca teclas presionadas
    teclas = pygame.key.get_pressed()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
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
    Colisiones(lista_alien, lista_proyectil, ancho_imagen)

    # Actualiza la cantidad de proyectiles
    largo_lista_proy = len(lista_proyectil)

    # Llamado para desplazar los proyectiles y las estrellas
    estrellas.actualizar_pos(lista_estrella, pantalla)
    proyectiles.mover_proyectil(largo_lista_proy)

    # Si se destruyen todos los aliens agrega más
    if len(lista_alien) == 0:
        iniciar_aliens()
        cant_alien += 7
        siguiente = True

    # Desplaza los aliens
    if ciclos == 0 and cont == 10:
        otra_variable.mover_alien(lista_alien, ciclos)
        cont = 0
    if ciclos == 1 and cont == 10:
        otra_variable.mover_alien(lista_alien, ciclos)
        cont = 0
        
    if contador2 == 20 and ciclos == 0:
        cantMov += 1
        contador2 = 0
        if cantMov == 3:
            cantMov = 0
            ciclos = 1

    if contador2 == 20 and ciclos == 1:
        cantMov += 1
        contador2 = 0
        if cantMov == 3:
            cantMov = 0
            ciclos = 0
            
    cont += 1
    contador2 += 1

    # Actualiza la posición x,y del jugador y lo dibuja en pantalla
    jugador1.actualizar_pos(velocidad, teclas) 
    jugador1.dibujar(pantalla)
    
    # Imprime en pantalla todos los gráficos
    pygame.display.flip()

    reloj.tick(75)
    
pygame.quit()
