import pygame

pygame.init()
pantalla=pygame.display.set_mode((400,300))
salir=False
reloj=pygame.time.Clock()
perso=pygame.image.load("adam2.png").convert_alpha()
muro=pygame.image.load("muro.png").convert_alpha()
muro2=pygame.image.load("muro2.png").convert_alpha()
(x,y)=(100,100)
vx=0
vy=0
#r1=pygame.Rect(450,70,25,50)
#r2=pygame.Rect(10,70,40,40)
sprite1=pygame.sprite.Sprite()
sprite1.image=perso
sprite1.rect=perso.get_rect()
sprite1.rect.top = 70
sprite1.rect.left = 200

sprite2=pygame.sprite.Sprite()
sprite2.image=muro
sprite2.rect=muro.get_rect()
sprite2.rect.top = 70
sprite2.rect.left = 10

sprite3=pygame.sprite.Sprite()
sprite3.image=muro2
sprite3.rect=muro2.get_rect()
sprite3.rect.top = 70
sprite3.rect.left = 300

while salir!=True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vx-=10
            if event.key == pygame.K_RIGHT:
                vx+=10
            if event.key == pygame.K_w:
                vy+=10
            if event.key == pygame.K_s:
                vy-=10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vx=0
            if event.key == pygame.K_RIGHT:
                vx=0

    oldx=sprite1.rect.left
    sprite1.rect.move_ip(vx,0)
    if sprite1.rect.colliderect(sprite3.rect) or sprite1.rect.colliderect(sprite2.rect):
        sprite1.rect.left=oldx
        
    
    
    reloj.tick(20)
    pantalla.fill((255,255,255))
##    pantalla.blit(perso,(x,y))
##    pygame.draw.rect(pantalla,(0,0,0),r1)
##    pygame.draw.rect(pantalla,(0,0,0),r2)
    pantalla.blit(sprite1.image,sprite1.rect)
    pantalla.blit(sprite2.image,sprite2.rect)
    pantalla.blit(sprite3.image,sprite3.rect)
    pygame.display.update()

pygame.quit()
