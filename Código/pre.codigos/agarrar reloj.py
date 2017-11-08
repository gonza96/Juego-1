import pygame

def main():
    pygame.init()
    pantalla=pygame.display.set_mode([800,600])
    pygame.display.set_caption("Juego Lanz")
    salir=False
    reloj=pygame.time.Clock()
    perso=pygame.image.load("jug.png").convert_alpha()
    gato=pygame.image.load("clock.png").convert_alpha()
    blanco=(255,255,255)
    rojo=(255,0,0)
    azul=(0,0,255)
    GREEN=(154,211,171)
    WHITE=(255,255,255)
    

    
    sprite1=pygame.sprite.Sprite()
    sprite1.image=perso
    sprite1.rect=perso.get_rect()
    sprite1.rect.top=300
    sprite1.rect.left=50

    sprite2=pygame.sprite.Sprite()
    sprite2.image=gato
    sprite2.rect=gato.get_rect()
    sprite2.rect.top=200
    sprite2.rect.left=50
 
    

    #loop principal
    while salir !=True:
        #recorro todos los eventos producidos
        for event in pygame.event.get():
           #si el evento es del tpo pygame.quit(cruz de la ventana) salir del while 
            if event.type==pygame.QUIT:
               salir=True
            if event.type ==pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                   sprite1.rect.move_ip(-20,0)
                if event.key==pygame.K_RIGHT:
                    sprite1.rect.move_ip(20,0)
                if event.key==pygame.K_UP:
                    sprite1.rect.move_ip(0,-20)
                if event.key==pygame.K_DOWN:
                    sprite1.rect.move_ip(0,20)
                    
        if event.type==pygame.MOUSEBUTTONDOWN:
                if sprite1.rect.colliderect(sprite2.rect):
                        sprite2.rect.top=10000
                        sprite2.rect.left=10000

      
          
        reloj.tick(20) #fijo a 20fps
        pantalla.fill(blanco)
       
        pantalla.blit(sprite1.image,sprite1.rect)
        pantalla.blit(sprite2.image,sprite2.rect)
        pygame.display.update()#actualizo display
   
   
    
    
    


    pygame.quit()

main()
