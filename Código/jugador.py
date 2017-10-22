import pygame
from main import *
from menu import *
from aliens import *

ROJO = (255, 0, 0)

# Definición de la clase jugador
class Jugador(pygame.sprite.Sprite):
    
    def __init__(self, imagen, velocidad, pantalla):
        super().__init__()
        
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = pantalla.get_width() / 2 - self.image.get_width() / 2
        self.rect.y = pantalla.get_height() - self.image.get_height()
        self.velocidad = velocidad

    # Actualiza la posición del jugador
    def actualizar_pos(self, velocidad, teclas, pantalla):
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

    # Imprime en pantalla al jugador
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)

    # Comprueba si hay colisión entre el jugador y los aliens 
    def colision_alien(self, lista_alien, pantalla):
        rect_alien = (0, 0, 0, 0)
        fuente_perder = pygame.font.Font(None, 50)
        texto_perder = fuente_perder.render("Perdiste", 1, (ROJO))
        texto_reiniciar = fuente_perder.render("Pulsa r para volver a iniciar", 1, (ROJO))
        rect_texto_r = texto_reiniciar.get_rect()
        rect_texto_r.centerx = pantalla.get_rect().centerx
        rect_texto_r.centery = 500
        rect_texto = texto_perder.get_rect()
        rect_texto.centerx = pantalla.get_rect().centerx
        rect_texto.centery = pantalla.get_rect().centery

        nueva_partida = False
        
        for i in range(len(lista_alien)):
            rect_alien = (lista_alien[i][0], lista_alien[i][1], 32, 32)
            if self.rect.colliderect(rect_alien):
                while not nueva_partida:
                    tecla = pygame.key.get_pressed()
                    pantalla.blit(texto_perder, rect_texto)
                    pantalla.blit(texto_reiniciar, rect_texto_r)
                    pygame.display.flip()

                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT or tecla[pygame.K_r]:
                            nueva_partida = True
                            self.rect.x = pantalla.get_width() / 2 - self.image.get_width() / 2
                            self.rect.y = pantalla.get_height() - self.image.get_height()
                            iniciar_aliens(73)
                            nueva_partida = True
                   
