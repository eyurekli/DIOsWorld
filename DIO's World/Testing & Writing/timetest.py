#This program is to test sounds, physics, random movements and cooldowns
#January 19

import random

import time

import datetime

import pygame, sys
from pygame.locals import *

from pygame import mixer

pygame.init()

mixer.init()

white = (255,255,255)
GREEN = (0,128,0)
screen = pygame.display.set_mode((1200,720))
pygame.display.set_caption('Spritesheets')

punch_sound = pygame.mixer.Sound("punch.wav")


#-FPS Clock-#
FPS = 60
fpsClock = pygame.time.Clock()


cairoCity = pygame.image.load('cairo.jpg')
cairoCity = pygame.transform.scale(cairoCity, (1200,720))

capy = pygame.image.load('capy.png')


cooldown_movement = 0

def EnemyMovement():
    global x
    global cooldown_movement

    EnemyMoves = [1,2,3,4]
    EnemyAct = random.choice(EnemyMoves)

    if cooldown_movement == 0:
        if EnemyAct == 1 and x > 0:
            x -= 400

        elif EnemyAct == 2 and x < 1200:
            x += 350

        elif EnemyAct == 3 and x > 0:
            x -= 200
            cooldown_movement = 10

        elif EnemyAct == 4 and x < 1200:
            x += 250
            cooldown_movement = 10
            
        

neg = pygame.Surface(cairoCity.get_size())
neg.fill((255, 255, 255))
    


cooldown_sound = 0

x = 100
y = 100
while True:
    screen.fill(white)
    screen.blit(cairoCity, (0,0))
    screen.blit(capy, (x,y))
    neg.blit(capy, (0, 100), special_flags=pygame.BLEND_SUB)

    if cooldown_sound > 0:
        cooldown_sound -= 1

    if cooldown_movement > 0:
        cooldown_movement -= 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= 10
        if cooldown_sound == 0:
            pygame.mixer.Sound.play(punch_sound)
            cooldown_sound = 50

    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_SPACE]:
        y += 10


    #EnemyMovement()
    pygame.display.update()
    fpsClock.tick(FPS)
