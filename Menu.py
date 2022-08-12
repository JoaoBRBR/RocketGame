#importando pygame
import pygame
from pygame.locals import *
#random
from random import randint, random, random
#tamanho da tela
width = 600
height = 600
#iniciando pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo Sem Nome')

#variaveis
Menu = True
Fases = False
Endless = False
x=0
y=0
bx=randint(0,width)
by=randint(0,height)

#variaveis exemplo de gravidade
#posição de um objeto
posX = 300
posY = 300
#velocidade de um objeto
velX = 0
velY = 0
#gravidade
gravidade = 0.001


while True:

    #xy sao a posicao do mouse
    x, y = pygame.mouse.get_pos()

    #inicio eventos de clicks
    for event in pygame.event.get():
        #fechar janela
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            velY = -0.2
            if x > posX:
                velX=-1
            else:
                velX=1
            #aqui verificamos clicks do mouse
            if Menu == True and x > 240 and x < 360 and y > 250 and y < 366:
                Menu = False
                Fases = True
            if Menu == True and x > 240 and x < 360 and y > 370 and y < 460:
                Menu = False
                Endless = True
                posX = 300
                posY = 300
                velX = 0
                velY = 0
            if Menu == False and x > 20 and x < 120 and y > 20 and y < 70:
                Menu = True
                Endless = False
                Fases = False
    #final eventos de clicks

    # reloading da tela
    screen.fill((0, 0, 0))

    #Menu
    if Menu == True:
        font = pygame.font.SysFont(None, 40)
        img = font.render('Fases', True, (255,255,255))
        screen.blit(img, (240, 250))
        font = pygame.font.SysFont(None, 40)
        img = font.render('Endless', True, (255,255,255))
        screen.blit(img, (240, 370))
    else:
        font = pygame.font.SysFont(None, 40)
        img = font.render('Voltar', True, (255,255,255))
        screen.blit(img, (20, 20))
    #Fases
    if Fases == True:
        font = pygame.font.SysFont(None, 40)
        img = font.render('Aqui sao as Fases', True, (255,255,255))
        screen.blit(img, (300, 10))

    #Endless
    if Endless == True:
        font = pygame.font.SysFont(None, 40)
        img = font.render('Modo infinito', True, (255,255,255))
        screen.blit(img, (300, 10))

        #exemplo de gravidade
        #desenhar o objeto na posição
        pygame.draw.rect(screen,(255,0,0),(posX,posY,20,20))

        pygame.draw.rect(screen,(0,255,0),(bx,by,40,40))
        if posX > bx-20 and posX < bx+20 and posY > by-20 and posY < by+20:
            bx=randint(0,width)
            by=randint(0,height)
        # na posição adicionamos a velocidade
        posX += velX
        posY += velY
        # e na velocidade adicionamos a gravidade
        # so no Y
        velY += gravidade

        #colidir na parede
        if posX < 0 or posX > width:
            velX *= -1
        if posY > height-6:
            posY = height-6
            velY *= -1
            velY += 0.1
    # refresh da tela
    pygame.display.update()
