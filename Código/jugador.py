import pygame
from main import *
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
        
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)
