import pygame

lista_alien = []

# Función para mover los aliens
def mover_alien(lista_alien, ciclos):
            
    if len(lista_alien) > 0:
        for i in range(len(lista_alien)):
            if ciclos == 1:
                lista_alien[i][0] -= 1
            if ciclos == 0:
                lista_alien[i][0] += 1
                    
# Coprueba si hay colisiones entre los proyectiles y los aliens
def Colisiones(lista_alien, lista_proyectil, ancho_imagen, puntos):
    
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
                        puntos += 50
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
