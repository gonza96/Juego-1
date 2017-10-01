import pygame
from main import *

class Menu:
    "Representa un menú con opciones para un juego"
    
    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font(None, 50)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

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

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[pygame.K_UP] or k[pygame.K_DOWN] or k[pygame.K_RETURN]


    def imprimir(self, pantalla):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = 50
        x = pantalla.get_width() / 2 - 100
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

    texto = fuente.render("Ingrese nombre:", 1, (BLANCO))
    pantalla.blit(texto, (pantalla.get_width() / 2 - 100, pantalla.get_height() / 2 - 50))
    pygame.display.flip()
    teclas = pygame.key.get_pressed()
    nombre = str(teclas)
    
    jugar(cant_alien, nombre)

def dificultad():
    pass

def guardar():
    pass

def mostrar_opciones():

    opciones_config = [
    ("Dificultad", dificultad),
    ("Guardar partida", guardar)
   ] 
    menu_opciones = Menu(opciones_config)
    volver = False
    
    while not volver:

        teclas = pygame.key.get_pressed()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or teclas[pygame.K_q]:
                volver = True

        pantalla.blit(imagen_fondo, (0, 0))
        menu_opciones.actualizar()
        menu_opciones.imprimir(pantalla)

        pygame.display.flip()
        pygame.time.delay(10)

def cargar_partida():
    pass

def creditos():
    
    volver = False
    creditos_juego = fuente3.render("Agregar créditos...", 1, (BLANCO))
    while not volver:
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or teclas[pygame.K_q]:
                volver = True

        pantalla.blit(creditos_juego, (pantalla.get_width() / 2 - 210, pantalla.get_height() / 2 - 18))
        
        pygame.display.flip()
        pygame.time.delay(10)
    
    
def salir_del_programa():
    import sys
    print ("Gracias por utilizar este programa.")
    pygame.quit()
    sys.exit(0)


if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("Nuevo juego", comenzar_nuevo_juego),
        ("Cargar partida", cargar_partida),
        ("Opciones", mostrar_opciones),
        ("Creditos", creditos),
        ("Salir", salir_del_programa)
        ]
    
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                salir = True

        pantalla.blit(imagen_fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(pantalla)

        pygame.display.flip()
        pygame.time.delay(10)
