#DIO's World
#Made by Ekin Yurekli

#A game created using Python and PyGame inspired by Capcom's 1998 game, JoJo's Bizarre Adventure: Heritage for the Future
#and the manga/anime series JoJo's Bizarre Adventure, created by Hirohiko Araki


#-----------------SOURCES & CREDITS---------------------#
#
#Loading Spritesheets: Coding with Russ on YouTube
#https://www.youtube.com/watch?v=M6e3_8LHc7A&t=454s
#Please check the spritesheet.py file submitted for the spritesheet module
#
#-Spritesheet for DIO from:
#https://www.spriters-resource.com
#
#-Spritesheet for DIO and the World from user samandjared420 on Deviantart
#https://www.deviantart.com/samandjared420/art/DIO-Sprite-Sheet-691136875
#
#PyGame Keys:
#https://www.pygame.org/docs/ref/key.html
#
#--"How Can I Make a Sprite Move When a Key is Held Down"--#
#https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down
#
#--Pygame Mixer for Music & Sounds
#https://pythonprogramming.net/adding-sounds-music-pygame/
#
#--How to Make a Character/Object Jump--
#https://www.codingninjas.com/codestudio/library/making-an-object-jump-in-pygame
#
#Jotaro Kujo Spritesheet from:
#https://www.deviantart.com/jayhyperstarx/art/Mugen-Jotaro-Kujo-Sprite-Sheet-908212361
#
#Flipping images
#https://www.geeksforgeeks.org/pygame-flip-the-image/
#
#Creating Pygame Text WITH a rectangle
#https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
#---------------------------------------------#


#--------PyGame & Module Importing---------#
import pygame, sys

#This is our custom module made to be able to use spritesheets in every code
#Simply by importing it. The spritesheet codes can stay in the same Python file,
#but putting spritesheets in different files allows us to reuse them easily if we were to use the same spritesheet

#Spritesheet for DIO
import spritesheet

#Spritesheet for the World, DIO's stand ability
import spritesheet2

#Spritesheet for Jotaro Kujo
import spritesheet3 

from pygame.locals import *
from pygame import mixer

#Imports the Random Module
import random

pygame.init()
#------------------------------------------#

#------------MUSIC & SOUND-----------------#

#Activates the Mixer module
mixer.init()

#Sets volume of the Music
mixer.music.set_volume(0.1)

#Variables for chosen sound files to play
punch_sound = pygame.mixer.Sound("SFX/punch.wav")
mixer.Sound.set_volume(punch_sound, 0.5)

zawarudocall = pygame.mixer.Sound("SFX/zawarudocall.wav")
mixer.Sound.set_volume(zawarudocall, 1)

dioweak = pygame.mixer.Sound("SFX/dioweak.wav")
diomedium = pygame.mixer.Sound("SFX/diomedium.wav")
dioheavy = pygame.mixer.Sound("SFX/dioheavy.wav")

#I downloaded these 3 SFX to use them for Dio's stand the World's attacks,
#but unfortunately there wasn't much time to code the World more in detail

mudaweak = pygame.mixer.Sound("SFX/mudaweak.wav")
mudamedium = pygame.mixer.Sound("SFX/mudamedium.wav")
mudaheavy = pygame.mixer.Sound("SFX/mudaheavy.wav")

menudown = pygame.mixer.Sound("SFX/menudown.wav")
mixer.Sound.set_volume(menudown, 0.8)

menuselect = pygame.mixer.Sound("SFX/menuselect.wav")
mixer.Sound.set_volume(menuselect, 0.4)

mudaheavy = pygame.mixer.Sound("SFX/mudaheavy.wav")
mixer.Sound.set_volume(mudaheavy, 0.8)

zawarudo = pygame.mixer.Sound("SFX/zawarudoshout.wav")
#-------------------------------------------#



#---------------COLORS & SCREEN---------------#
white = (255,255,255)
GREEN = (0,128,0)
BLUE = (128,128,255)
Red = (255,0,0)
Black = (0,0,0)
blue = (0, 0, 128)
yellow = (255, 209, 53)

screen = pygame.display.set_mode((1200,720))
pygame.display.set_caption("DIO's World")


#---------Variables & Misc -------------------#

#-FPS Clock-#
FPS = 60
fpsClock = pygame.time.Clock()

#DIO Location
yd = 400
xd = 0
movecount = 0
direction = "Right"

X = 600
Y = 500

#Menu Variables
MainMenu = True
MainGame = False
Start = True
SelectionScreen = False
selection = 1
ObjectiveSelect = False
StageSelect = False
Controls = False


#Animation Variables
attackanim = 0

#Jump Variables
is_jump = False
vel = 10
mass = 1
cooldown_j = 0

#Direction Variable
direction = "Right"

#Cooldown Variables

#After looking at how many cooldown variables there are,
#I think it was better to create a list with the cooldowns and substract -1
#from the entire list if it is possible.
cooldown_attack = 0
cooldown_sound = 0       
cooldown_stand = 0
cooldown_timestop = 0
cooldown_movement = 0
cooldown_dash = 0

#The World Variables
StandReveal = False
timestopcount = 0
duration_timestop = 0
timestop = False

#Enemy Variable
enemy = 1

#---------------------------------------------#

#---------------IMAGES------------------------#

#Cairo City Map
cairoCity = pygame.image.load('Background/cairo.jpg')
cairoCity = pygame.transform.scale(cairoCity, (1200,720))

#Negative Effect Cairo City, used when the World stops time
cairoCityNeg = pygame.image.load('Background/caironeg.jpg')
cairoCityNeg = pygame.transform.scale(cairoCityNeg, (1200,720))

#Clock Tower Map
ClockTower = pygame.image.load('Background/clocktower.jpg')
ClockTower = pygame.transform.scale(ClockTower, (1200,720))

#Negative Effect Clock Tower
ClockTowerNeg = pygame.image.load('Background/clocktowerneg.jpg')
ClockTowerNeg = pygame.transform.scale(ClockTowerNeg, (1200,720))

#Default Map is Cairo City
CurrentMap = cairoCity
NegMap = cairoCityNeg

#Main Menu Background Image
mainMenu = pygame.image.load('Background/menu.png')
mainMenu = pygame.transform.scale(mainMenu, (1200,720))

#Controls Image
controls = pygame.image.load('Background/controlz2.png')
controls = pygame.transform.scale(controls, (894,256))


#DIO SpriteSheet
sprite_sheet_image = pygame.image.load('Sprites/dio.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)


#The WORLD SpriteSheet
sprite_sheet_world = pygame.image.load('Sprites/theworld.png').convert_alpha()
sprite_sheet2 = spritesheet2.SpriteSheetWorld(sprite_sheet_world)

#Jotaro Kujo Spritesheet
sprite_sheet_jotaro = pygame.image.load('Sprites/jotaro.png').convert_alpha()
sprite_sheet3 = spritesheet3.SpriteSheetJotaro(sprite_sheet_jotaro)

#Functions & Misc

#DIO's Sprites While Standing
standing_frame_0 = sprite_sheet.get_image(0, 0, 69, 125, 2, GREEN)
standing_frame_1 = sprite_sheet.get_image(1, 0, 69, 125, 2, GREEN)
standing_frame_2 = sprite_sheet.get_image(2, 0, 69, 125, 2, GREEN)
standing_frame_3 = sprite_sheet.get_image(3, 0, 69, 125, 2, GREEN)
standing_frame_4 = sprite_sheet.get_image(4, 0, 69, 125, 2, GREEN)

#The World Default Sprite
the_world_frame0 = sprite_sheet2.get_image(0, 0, 101, 150, 1.8, BLUE)   


#Jotaro Sprites Test
j_standing_frame0 = sprite_sheet3.get_image(0, 0, 80, 120, 2, GREEN)
j_current_frame = j_standing_frame0

sp_standing_frame0 = sprite_sheet3.get_image(8.66, 0, 106, 128, 2, GREEN)
j_current_frame = sp_standing_frame0


#----------------------------------------------#
#Enemies & Models

#Sets up the enemy depending on what is chosen in the menu
def Enemy_Select():

    global enemyselect
    global enemy_x
    global enemy_y
    global enemy_life
    global enemy
    global enemy_width
    global j_current_frame
    global j_standing_frame0


    car = pygame.image.load('Sprites/car.png')
    car = pygame.transform.scale(car, (860 / 1.75,392 / 1.75))
    car_x = 600
    car_y = 430

    capybara = pygame.image.load('Sprites/capy.png')
    capybara = pygame.transform.scale(capybara, (458 / 2, 458 / 2))
    cap_x = 600
    cap_y = 430

    jx = 600
    jy = 400

    if enemy == 2:
        enemyselect = capybara
        enemy_x = cap_x
        enemy_y = cap_y
        enemy_life = 5000
        enemy_width = 300
        
    elif enemy == 1:
        enemyselect = car
        enemy_x = car_x
        enemy_y = car_y
        enemy_life = 5000
        enemy_width = 492

    elif enemy == 3:
        enemyselect = j_current_frame
        enemy_x = jx
        enemy_y = jy
        enemy_life = 10000
        enemy_width = 150
        

#Counts enemy life and displays a health bar
def Enemy_Life():
    global enemy_life
    global capybara
    global enemy
    global MainMenu
    global MainGame
    global life_divider
    global duration_timestop

    if enemy == 1 or enemy == 2:
        life_divider = 6.25

    elif enemy == 3:
        life_divider = 12.5
        
    

    #Enemy/Object Life Bar
    if enemy_life > 0:
        pygame.draw.rect(screen,GREEN,[200,10,enemy_life / life_divider,20],0)
        pygame.draw.rect(screen,GREEN,[200,10,800,20],5)
    
    elif enemy_life <= 0 and enemy_life > -300:
        font3 = pygame.font.Font('freesansbold.ttf', 90)
        KO = font3.render("K.O.!!!", True, GREEN, yellow)
        KORect = KO.get_rect()
        KORect.center = (X, Y-300)
        screen.blit(KO, KORect)
        duration_timestop = 0
        cooldown_timestop = 0

        enemy_life -= 1

    elif enemy_life <= -300:
        font4 = pygame.font.Font('freesansbold.ttf', 60)
        YouWin = font4.render("Player 1 Wins!", True, GREEN, yellow)
        YWRect = YouWin.get_rect()
        YWRect.center = (X, Y-300)
        screen.blit(YouWin, YWRect)

        enemy_life -= 1

#Gives random moves to Capybara and Jotaro depending on the number taken from the list
def EnemyMovement():
    global enemy_x
    global cooldown_movement
    global enemy
    global enemy_life
    global duration_timestop
    global enemy_direction
    global enemy_distance


    #Random Moves of Capybara
    if enemy == 2 and enemy_life > 0 and duration_timestop == 0:
        EnemyMoves = [1,2,3,4]
        EnemyAct = random.choice(EnemyMoves)

        if cooldown_movement == 0:
            if EnemyAct == 1 and enemy_x > 229:
                enemy_x -= 200
                

            elif EnemyAct == 2 and enemy_x < 950:
                enemy_x += 200
                

            elif EnemyAct == 3 and enemy_x > 229:
                enemy_x -= 100
                

            elif EnemyAct == 4 and enemy_x < 950:
                enemy_x += 150

            cooldown_movement = 25

    #Random Moves of Jotaro #Jotaro can move 2 seconds during the timestop in the anime/manga,
    #so he can move when there is 2 seconds left compared to Capybara
            
    if enemy == 3 and enemy_life > 0 and duration_timestop <= 200:

        # introduce variables to keep track of the movement direction and distance

        if cooldown_movement == 0:
            EnemyMoves = [1,2,3,4]
            EnemyAct = random.choice(EnemyMoves)
            
            enemy_direction = 0

            if EnemyAct == 1 and enemy_x > 229:
                enemy_direction = -5
            elif EnemyAct == 2 and enemy_x < 950:
                enemy_direction = 5
            elif EnemyAct == 3 and enemy_x > 229:
                enemy_direction = -10
            elif EnemyAct == 4 and enemy_x < 950:
                enemy_direction = 10

            cooldown_movement = 10

        elif cooldown_movement > 0:
            
            if enemy_x > 229 and enemy_direction == -5 or enemy_direction == -10:
                enemy_x += enemy_direction     
            elif enemy_x < 950 and enemy_direction == 5 or enemy_direction == 10:         
                enemy_x += enemy_direction


#----------------------------------------------#
##---------Movements and Abilities---------##
#----------------------------------------------#
#DIO's Walking Program
def DioWalking():

    global cooldown_attack
    global xd
    global direction
    global keys
    
    if keys[pygame.K_LEFT] and xd >= 0:
        xd -= 5
        direction = "Left"
        DioWalkingAnimation()
        cooldown_attack = 1

    if keys[pygame.K_RIGHT] and xd <= 1100:
        xd += 5
        direction = "Right"
        DioWalkingAnimation()
        cooldown_attack = 1

#DIO's Walking Animation  
def DioWalkingAnimation():
    global movecount
    global current_frame

    walk_frame_0 = sprite_sheet.get_image(0, 4.6, 69, 125, 2, GREEN)
    walk_frame_1 = sprite_sheet.get_image(1, 4.6, 69, 125, 2, GREEN)
    walk_frame_2 = sprite_sheet.get_image(2, 4.6, 75, 125, 2, GREEN)
    walk_frame_3 = sprite_sheet.get_image(3, 4.6, 75, 125, 2, GREEN)
    walk_frame_4 = sprite_sheet.get_image(4.1, 4.6, 75, 125, 2, GREEN)
    walk_frame_5 = sprite_sheet.get_image(5.06, 4.6, 75, 125, 2, GREEN)
    walk_frame_6 = sprite_sheet.get_image(7.59, 4.6, 60, 125, 2, GREEN)
    walk_frame_7 = sprite_sheet.get_image(8.55, 4.6, 60, 125, 2, GREEN)
    walk_frame_8 = sprite_sheet.get_image(9.5, 4.6, 60, 125, 2, GREEN)
    walk_frame_9 = sprite_sheet.get_image(8.46, 4.6, 75, 125, 2, GREEN)
    walk_frame_10 = sprite_sheet.get_image(8.3, 4.6, 85, 125, 2, GREEN)


    if movecount >= 0 and movecount < 5:
        current_frame = walk_frame_0
        movecount += 1
        
    elif movecount >= 5 and movecount < 10:
        current_frame = walk_frame_1
        movecount += 1
        
    elif movecount >= 10  and movecount < 15:
        current_frame = walk_frame_2
        movecount += 1
        
    elif movecount >= 15 and movecount < 20:
        current_frame = walk_frame_3
        movecount += 1

    elif movecount >= 20 and movecount < 25:
        current_frame = walk_frame_4
        movecount += 1
        
    elif movecount >= 25 and movecount < 30:
        current_frame = walk_frame_5
        movecount += 1

    elif movecount >= 30 and movecount < 35:
        current_frame = walk_frame_6
        movecount += 1
        
    elif movecount >= 35 and movecount < 40:
        current_frame = walk_frame_7
        movecount += 1
        
    elif movecount >= 40 and movecount < 45:
        current_frame = walk_frame_8
        movecount += 1
        
    elif movecount >= 45 and movecount < 50:
        current_frame = walk_frame_9
        movecount += 1

    elif movecount >= 50 and movecount < 55:
        current_frame = walk_frame_10
        movecount += 1

    elif movecount == 55:
        current_frame = walk_frame_0
        movecount = 0
    
#----------------------------------------------#
#DIO's Dash Animation #CURRENTLY DISABLED
#the dash animation would sometimes glitch in with the walk animation
#and just cause DIO to walk fast as dashing without any cooldown.
#Last time I plugged the function, there were still problems. I still kept it to use it in the future.
        
def DioDashing():
    global movecount
    global current_frame
    global cooldown_dash
    global direction
    global xd

    #DIO's Sprites While Dashing
    dash_frame_0 = sprite_sheet.get_image(0, 6.8, 60, 125, 2, GREEN)
    dash_frame_1 = sprite_sheet.get_image(0.45, 7, 125, 125, 2, GREEN)
    dash_frame_2 = sprite_sheet.get_image(1.44, 7, 125, 125, 2, GREEN)
    dash_frame_3 = sprite_sheet.get_image(3.33, 7, 90, 125, 2, GREEN)

    if movecount >= 0 and movecount < 10:
        current_frame = dash_frame_0
        movecount += 1
        
    if movecount >= 10 and movecount < 15:
        current_frame = dash_frame_1
        movecount += 1
        
        
    if movecount >= 15 and movecount < 20:
        current_frame = dash_frame_2
        movecount += 1
        
    if movecount >= 20 and movecount < 30:
        current_frame = dash_frame_3
        movecount += 1
        
    if movecount >= 30 and movecount < 40:
        current_frame = dash_frame_2
        movecount += 1
        
    if movecount >= 40 and movecount < 50:
        current_frame = dash_frame_1
        movecount += 1

    if movecount == 50:
        current_frame = dash_frame_0
        movecount = 0
        #cooldown_dash = 5
        
    if direction == "Right":
        xd += 15
    elif direction == "Left":
        xd -= 15
        

#----------------------------------------------#

#DIO's Attacks    

#It is named "New" because this was my 2nd attempt at animating the attacks
#and also register hits
        
def DioAttackNew():
    global current_frame
    global attackanim
    global cooldown_attack
    global direction
    global xd
    global yd
    global attackw_frame_0
    global attackw_frame_1
    global attackw_frame_2
    global enemy_life
    global enemy_width
    global cooldown_sound

    #Sets the hitbox range variables. These are here just to defy it. The real hitbox range is below.
    x_hit = xd + 300
    y_hit = yd + 100

    #Weak Attack Frames
    attackw_frame_0 = sprite_sheet.get_image(0, 10.4, 55, 125, 2, GREEN)
    attackw_frame_1 = sprite_sheet.get_image(0.45, 10.87, 120, 120, 2, GREEN)
    attackw_frame_2 = sprite_sheet.get_image(1.95, 10.42, 91, 125, 2, GREEN)

    #Medium Attack Frames
    attackm_frame_0 = sprite_sheet.get_image(0, 11.48, 80, 125, 2, GREEN)
    attackm_frame_4 = sprite_sheet.get_image(2.88, 13.16, 133, 110, 2, GREEN)
    attackm_frame_5 = sprite_sheet.get_image(6.45, 11.48, 80, 125, 2, GREEN)
    attackm_frame_6 = sprite_sheet.get_image(4.37, 11.48, 136, 125, 2, GREEN)
    attackm_frame_8 = sprite_sheet.get_image(7.31, 11.48, 120, 125, 2, GREEN)
    

    #Heavy Attack Frames
    attackh_frame_0 = sprite_sheet.get_image(0, 12.02, 75, 130, 2, GREEN)
    attackh_frame_1 = sprite_sheet.get_image(0.9, 12.02, 85, 130, 2, GREEN)
    attackh_frame_2 = sprite_sheet.get_image(1.1, 13.57, 150, 116, 2, GREEN)
    attackh_frame_3 = sprite_sheet.get_image(2.52, 12.02, 125, 130, 2, GREEN)
    attackh_frame_9 = sprite_sheet.get_image(11.34, 12.02, 90, 130, 2, GREEN)


    #I adjusted them here
    if direction == 'Right':
        x_hit = xd + 200

    if direction == 'Left':
        x_hit = xd - 75
        

    #A cooldown has been set up so that attacks cannot be done while walking
    if keys and cooldown_attack == 0:

        attackanim += 1
        
        #Weak Attack
        if keys[pygame.K_a]:
            
            if attackanim == 8:
                pygame.mixer.Sound.play(dioweak)
                
            if attackanim >= 0 and attackanim < 8:
                current_frame = attackw_frame_0
                
            elif attackanim >= 8 and attackanim < 16:
                current_frame = attackw_frame_1
                
            #Registers the hit
            elif attackanim >= 16 and attackanim < 24:
                current_frame = attackw_frame_2
            
        
        #Medium Attack
        if keys[pygame.K_w]:
            
            if attackanim == 8:
                pygame.mixer.Sound.play(diomedium)
                
            if attackanim >= 0 and attackanim < 8:
                current_frame = attackm_frame_0
                
            elif attackanim >= 8 and attackanim < 16:
                current_frame = attackm_frame_4
                
            elif attackanim >= 16 and attackanim < 20:
                current_frame = attackm_frame_5
                
            elif attackanim >= 20 and attackanim < 22:
                current_frame = attackm_frame_6

            elif attackanim >= 22 and attackanim < 24:
                current_frame = attackm_frame_8
                
        #Heavy Attack
        if keys[pygame.K_d]:

            if attackanim == 8:
                pygame.mixer.Sound.play(dioheavy)
                
            if attackanim >= 0 and attackanim < 8:
                current_frame = attackh_frame_0
            elif attackanim >= 8 and attackanim < 16:
                current_frame = attackh_frame_1

            elif attackanim >= 16 and attackanim < 20:
                current_frame = attackh_frame_2
                
            elif attackanim >= 20 and attackanim < 24:
                current_frame = attackh_frame_3

        if attackanim == 24:
            attackanim = 0

        #If attack animation reaches 24 and the hit is in range, a hit is registered and a punch sound is played  
        if x_hit >= enemy_x and x_hit <= enemy_x + enemy_width and enemy_life > 0 and attackanim == 16:
            
            if keys[pygame.K_a]:
                enemy_life -= 100
                pygame.mixer.Sound.play(punch_sound)
                
            elif keys[pygame.K_w]:
                enemy_life -= 150
                pygame.mixer.Sound.play(punch_sound)
                    
            elif keys[pygame.K_d]:
                enemy_life -= 200
                pygame.mixer.Sound.play(punch_sound)
                

#----------------------------------------------#
#DIO's Jump       
def DioJump():
    global yd
    global is_jump
    global vel
    global mass
    global F_orce
    global cooldown_j
    global cooldown_attack
    global current_frame

    #DIO's jumping frames
    jump_frame_0 = sprite_sheet.get_image(0, 7.18, 85, 155, 2, GREEN)
    jump_frame_1 = sprite_sheet.get_image(1, 7.18, 85, 155, 2, GREEN)
    jump_frame_2 = sprite_sheet.get_image(2.02, 7.18, 83, 155, 2, GREEN)
    jump_frame_3 = sprite_sheet.get_image(2.89, 7.18, 85, 155, 2, GREEN)
    jump_frame_4 = sprite_sheet.get_image(3.7, 7.18, 90, 155, 2, GREEN)
    jump_frame_5 = sprite_sheet.get_image(4.62, 7.18, 92, 155, 2, GREEN)
    jump_frame_6 = sprite_sheet.get_image(6.30, 7.18, 85, 155, 2, GREEN)
    jump_frame_7 = sprite_sheet.get_image(8.85, 7.18, 70, 155, 2, GREEN)
    jump_frame_8 = sprite_sheet.get_image(11.48, 7.18, 60, 155, 2, GREEN)
    jump_frame_9 = sprite_sheet.get_image(12.5, 7.18, 60, 155, 2, GREEN)


    if is_jump == False:
        if keys[pygame.K_UP] and cooldown_j == 0:
            is_jump = True
            
  
    if is_jump == True:
        #Prevents attacks from being made mid-air
        cooldown_attack = 1
        
        F_orce = (1 / 2) * mass *(vel**2)
        yd -= F_orce

        vel = vel-1

        #Animation of the jump
        if vel <= 10 and vel > 8:
            current_frame = jump_frame_0
        elif vel <= 8 and vel > 6:
            current_frame = jump_frame_1
        elif vel <= 6 and vel > 4:
            current_frame = jump_frame_2
        elif vel <= 4 and vel > 2:
            current_frame = jump_frame_3
        elif vel <= 2 and vel > 0:
            current_frame = jump_frame_4
        elif vel <= 0 and vel > -2:
            current_frame = jump_frame_5
        elif vel <= -2 and vel > -4:
            current_frame = jump_frame_6
        elif vel <= -4 and vel > -6:
            current_frame = jump_frame_7
        elif vel <= -6 and vel > -8:
            current_frame = jump_frame_8
        elif vel <= -8 and vel > -10:
            current_frame = jump_frame_9
        
        #Makes DIO fall down
        if vel<0:
            mass = -1
        if vel ==-11:
            is_jump = False
            vel = 10
            mass = 1
            cooldown_j = 10
            
        pygame.time.delay(1)

#----------------------------------------------#

#Turning on and off DIO's Stand Power, the WORLD
def StandPower():

    global StandReveal
    global StandPower
    global cooldown_stand
    global direction
    global current_frame_the_world
    global cooldown_timestop
    global current_frame
    global timestopcount
    global duration_timestop
    global timestop

    
    #Setting up frames for DIO and The World during the timestop
    the_world_frame_timestop = sprite_sheet2.get_image(10.69, 4.7, 144, 150, 1.8, BLUE)
    jump_frame_7 = sprite_sheet.get_image(8.85, 7.18, 70, 155, 2, GREEN)

    #Turns off stands and gives a cooldown
    if keys[pygame.K_z] and cooldown_stand == 0 and StandReveal == True:
        StandReveal = False
        cooldown_stand = 50
        
    #Turns on stands and gives a cooldown
    if keys[pygame.K_z] and cooldown_stand == 0 and StandReveal == False:
        StandReveal = True
        cooldown_stand = 50
        pygame.mixer.Sound.play(zawarudocall)

    #If stands are on, it enables the timestop
    if StandReveal == True:
        if keys[pygame.K_x] and cooldown_timestop == 0:
            timestop = True

        if timestop == True:
            if timestopcount == 0:
                pygame.mixer.Sound.play(zawarudo)

            timestopcount += 1
            
            if timestopcount > 0 and timestopcount < 75:
                current_frame = jump_frame_7
                current_frame_the_world = the_world_frame_timestop

            if timestopcount == 150:
                duration_timestop = 500
                cooldown_timestop = 1500
                timestopcount = 0
                timestop = False

            


#----------------------------------------------#

#------------COOLDOWNS-----------#

#-Prevents certain abilities from getting used over and over and buttons from giving too many inputs
def Cooldown():
    global cooldown_j
    global cooldown_dash
    global cooldown_attack
    global cooldown_stand
    global cooldown_sound
    global cooldown_movement
    global cooldown_timestop
    global duration_timestop
    
    if cooldown_j > 0:
        cooldown_j -= 1
        
    if cooldown_dash > 0:
        cooldown_dash -= 1

    if cooldown_attack > 0:
        cooldown_attack -= 1

    if cooldown_stand > 0:
        cooldown_stand -= 1

    if cooldown_sound > 0:
        cooldown_sound -= 1

    if cooldown_movement > 0:
        cooldown_movement -= 1

    if cooldown_timestop > 0:
        cooldown_timestop -= 1
        if cooldown_timestop == 0:
            print("Cooldown is over")

    if duration_timestop > 0:
        duration_timestop -= 1
        mixer.music.play()

        

#------------DIRECTIONS-----------#
#Changes the Direction of DIO's Sprites by creating a temporary copy of the current sprite that is horizontally flipped
def Direction():
    global direction
    global img_copy
    global current_frame
    global current_frame_the_world
    global img_copy_world
    global j_current_frame
    global img_copy_jotaro

    #Flips DIO and The World
    if direction == "Left":
        img_copy = current_frame.copy()
        current_frame = pygame.transform.flip(img_copy, True, False)

        img_copy_world = current_frame_the_world.copy()
        current_frame_the_world = pygame.transform.flip(img_copy_world, True, False)

    #Flips Jotaro
    elif direction == "Right":
        img_copy_jotaro = j_current_frame.copy()
        j_current_frame = pygame.transform.flip(img_copy_jotaro, True, False)

#The Start/Title Screen Function
def StartScreen():
    global font1
    global font2
    global title
    global start
    global titleRect
    global startRect
    global keys
    global cooldown_menu

    #Displays text
    font1 = pygame.font.Font('freesansbold.ttf', 90)
    title = font1.render("DIO's World", True, GREEN, yellow)
    titleRect = title.get_rect()
    titleRect.center = (X, Y)

    font2 = pygame.font.Font('freesansbold.ttf', 45)
    start = font2.render("Press SPACE to Start", True, GREEN, yellow)
    startRect = start.get_rect()
    startRect.center = (X, Y+100)

    #Blits the Main Menu Background and Title Text
    screen.blit(mainMenu, (0,0))
    screen.blit(title, titleRect)
    screen.blit(start, startRect)


#Sets up the Main Menu itself
def MainMenuFunctions():

    global cooldown_menu
    global SelectionScreen
    global keys
    global Start
    global font2
    global MainMenu
    global MainGame
    global selection
    global ObjectiveSelect
    global enemyselect
    global enemy_x
    global enemy_y
    global enemy_life
    global enemy
    global enemy_width
    global StageSelect
    global StageSelector
    global Controls

    if Start == True:
        StartScreen()
        
        #Moves on to the Select Screen after the Title/Start Screen
        if keys[pygame.K_SPACE]:
            pygame.mixer.Sound.play(menuselect)
            Start = False
            cooldown_menu = 50
            SelectionScreen = True

    #Displays the Selection Screen 
    if SelectionScreen == True:
        Selection()

    #Displays the Enemy/Objective Select Screen
    if ObjectiveSelect == True:
        ObjectiveSelection()

    #Displays the Stage Select Screen
    if StageSelect == True:
        StageSelector()

    if Controls == True:
        ControlsDisplay()

    #Determines the Enemy once everything is set
    Enemy_Select()
#------------------------------------------------------------------------------#

#Displats the main menu selection screen
def Selection():
    global ObjectiveSelect
    global selection
    global cooldown_menu
    global keys
    global MainMenu
    global MainGame
    global SelectionScreen
    global StageSelect
    global StageSelector
    global Controls

    #Four colorings for the selections
    selcolor1 = yellow
    selcolor2 = yellow
    selcolor3 = yellow
    selcolor4 = yellow
    
    #Makes the current selection's square red
    if selection == 1:
        selcolor1 = Red
        
    elif selection == 2:
        selcolor2 = Red
        
    elif selection == 3:
        selcolor3 = Red
        
    elif selection == 4:
        selcolor4 = Red


    #Text Displays
    GameStart = font2.render("Play", True, GREEN, selcolor1)
    GameStartRect = GameStart.get_rect()
    GameStartRect.center = (X, Y-50)

    SelObj = font2.render("Select Objective", True, GREEN, selcolor2)
    SelObjRect = SelObj.get_rect()
    SelObjRect.center = (X, Y)

    SelStage = font2.render("Select Stage", True, GREEN, selcolor3)
    SelStageRect = SelStage.get_rect()
    SelStageRect.center = (X, Y+50)

    HowTo = font2.render("How to Play", True, GREEN, selcolor4)
    HowToRect = HowTo.get_rect()
    HowToRect.center = (X, Y+100)

    #Displays the text and main menu background
    screen.blit(mainMenu, (0,0))
    screen.blit(GameStart, GameStartRect)
    screen.blit(SelObj, SelObjRect)
    screen.blit(SelStage, SelStageRect)
    screen.blit(HowTo, HowToRect)

    #A cooldown for the menu so that the space button doesn't give too many inputs
    if cooldown_menu > 0:
        cooldown_menu -= 1

    if cooldown_menu == 0:
        if keys[pygame.K_DOWN]:
            selection += 1
            pygame.mixer.Sound.play(menudown)
            cooldown_menu = 10
            if selection > 4:
                selection = 1
        if keys[pygame.K_UP]:
            selection -= 1
            pygame.mixer.Sound.play(menudown)
            cooldown_menu = 10
            if selection < 1:
                selection = 4

        #Confirms selection
        if keys[pygame.K_SPACE]:

            #Starts the game
            if selection == 1:
                MainMenu = False
                MainGame = True
                StandReveal = False
                pygame.mixer.Sound.play(menuselect)
                mixer.music.load("OST/diotheme.wav")
                mixer.music.play()              

            #Enables the Enemy/Objective select screen
            if selection == 2:
                cooldown_menu = 10
                SelectionScreen = False
                ObjectiveSelect = True
                pygame.mixer.Sound.play(menuselect)
                selection = 1
                
            #Enables the Map Select Screen
            if selection == 3:
                cooldown_menu = 10
                SelectionScreen = False
                StageSelect = True
                pygame.mixer.Sound.play(menuselect)
                selection = 1

            if selection == 4:
                cooldown_menu = 10
                SelectionScreen = False
                Controls = True
                pygame.mixer.Sound.play(menuselect)
                selection = 1

            
#Enemy/objective Selection Function.
def ObjectiveSelection():

    global keys
    global cooldown_menu
    global selection
    global enemy
    global ObjectiveSelect
    global SelectionScreen

    #Four colorings for the selections
    selcolor1 = yellow
    selcolor2 = yellow
    selcolor3 = yellow
    selcolor4 = yellow
    
    #Makes the current selection's square red
    if selection == 1:
        selcolor1 = Red
        
    elif selection == 2:
        selcolor2 = Red
        
    elif selection == 3:
        selcolor3 = Red
        
    elif selection == 4:
        selcolor4 = Red

    #Displays texts
    Car2 = font2.render("Car", True, GREEN, selcolor1)
    Car2Rect = Car2.get_rect()
    Car2Rect.center = (X, Y-50)

    Capy = font2.render("Capybara", True, GREEN, selcolor2)
    CapyRect = Capy.get_rect()
    CapyRect.center = (X, Y)

    Jota = font2.render("Jotaro Kujo", True, GREEN, selcolor3)
    JotaRect = Jota.get_rect()
    JotaRect.center = (X, Y+50)

    #Displays the background and options to the screen
    screen.blit(mainMenu, (0,0))
    screen.blit(Car2, Car2Rect)
    screen.blit(Capy, CapyRect)
    screen.blit(Jota, JotaRect)

    if cooldown_menu > 0:
        cooldown_menu -= 1
        
    if cooldown_menu == 0:
        if keys[pygame.K_DOWN]:
            selection += 1
            pygame.mixer.Sound.play(menudown)
            cooldown_menu = 20
            if selection > 3:
                selection = 1
                
        if keys[pygame.K_UP]:
            selection -= 1
            pygame.mixer.Sound.play(menudown)
            cooldown_menu = 20
            if selection < 1:
                selection = 3

        if keys[pygame.K_SPACE]:
            cooldown_menu = 20
            if selection == 1:
                enemy = 1
            if selection == 2:
                enemy = 2
            if selection == 3:
                enemy = 3

            
            ObjectiveSelect = False
            SelectionScreen = True
            pygame.mixer.Sound.play(menuselect)
            cooldown_menu = 10

#Map/Stage Select Screen
def StageSelector():

    global keys
    global cooldown_menu
    global selection
    global enemy
    global ObjectiveSelect
    global SelectionScreen
    global CurrentMap
    global StageSelect
    global NegMap

    #Four colorings for the selections
    selcolor1 = yellow
    selcolor2 = yellow
    selcolor3 = yellow
    selcolor4 = yellow


    #Makes the current selection's square red
    if selection == 1:
        selcolor1 = Red
        
    elif selection == 2:
        selcolor2 = Red
        
    elif selection == 3:
        selcolor3 = Red
        
    elif selection == 4:
        selcolor4 = Red

    #Text Display
    CairoC = font2.render("Cairo City", True, GREEN, selcolor1)
    CairoCRect = CairoC.get_rect()
    CairoCRect.center = (X, Y-50)

    ClockT = font2.render("Clock Tower", True, GREEN, selcolor2)
    ClockTRect = ClockT.get_rect()
    ClockTRect.center = (X, Y)

    #Blits the background and all of the texts
    screen.blit(mainMenu, (0,0))
    screen.blit(CairoC, CairoCRect)
    screen.blit(ClockT, ClockTRect)

    if cooldown_menu > 0:
        cooldown_menu -= 1
        
    if cooldown_menu == 0:
        if keys[pygame.K_DOWN]:
            selection += 1
            pygame.mixer.Sound.play(menudown)
            cooldown_menu = 10
            if selection > 2:
                selection = 1
                
        if keys[pygame.K_UP]:
            selection -= 1
            pygame.mixer.Sound.play(menudown)
            cooldown_menu = 10
            if selection < 1:
                selection = 2

        #Confirms selection
        if keys[pygame.K_SPACE]: 
            if selection == 1:
                CurrentMap = cairoCity
                NegMap = cairoCityNeg
            if selection == 2:
                CurrentMap = ClockTower
                NegMap = ClockTowerNeg
                
            StageSelect = False
            SelectionScreen = True
            pygame.mixer.Sound.play(menuselect)
            cooldown_menu = 10

#Displays Controls
def ControlsDisplay():

    global Controls
    global SelectionScreen
    global Controls
    global cooldown_menu

    screen.blit(mainMenu, (0,0))
    screen.blit(controls, (153,400))

    if cooldown_menu > 0:
        cooldown_menu -= 1
        
    if cooldown_menu == 0:
        #Confirms selection
        if keys[pygame.K_SPACE]:
            cooldown_menu = 20
            pygame.mixer.Sound.play(menuselect)
            SelectionScreen = True
            Controls = False
    


#------------------------------------------------------------------------------#



###------------#Main Code#---------------------#
while True:

    #I put the variables here once again so that everything can return to normal
    #DIO Location
    yd = 400
    xd = 0
    movecount = 0
    direction = "Right"
    
    #Loads music
    mixer.music.load("OST/eyesofheaven.wav")
    mixer.music.play()

##-------------Main Menu---------------------#
    while MainMenu == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(white)
        keys = pygame.key.get_pressed()        
        MainMenuFunctions()
        pygame.display.update()
        fpsClock.tick(FPS)

        
##---------------Main Game Code--------------#
    while MainGame == True:
    
        screen.fill(white)

        #Displays the chosen map, Cairo City by default
        screen.blit(CurrentMap, (0,0))

        #Displays the maps with the negative colours if time is stopped by DIO
        if duration_timestop > 0:
            screen.blit(NegMap, (0,0))
            mixer.music.stop()


        #Frames for the characters if there is no movement from them
        j_current_frame = j_standing_frame0 #sp_standing_frame0
        current_frame = standing_frame_0
        current_frame_the_world = the_world_frame0


        #Allows user to quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #Checks keys being pressed
        keys = pygame.key.get_pressed()

        #Movements Keys
        DioWalking()

        #DIO's Jump Function
        DioJump()

        #DIO's Attacks Function
        DioAttackNew()

        #Cooldown function
        Cooldown()

        StandPower()

        EnemyMovement()

        #Direction function that reflects Dio's sprites depending on the direction.
        Direction()

        #Displays Enemy/Objective
        if enemy == 1 or enemy == 2:
            screen.blit(enemyselect, (enemy_x, enemy_y))
        if enemy == 3:
            screen.blit(j_current_frame, (enemy_x, enemy_y))

        
        if StandReveal == True:
            if direction == "Right":
                screen.blit(current_frame_the_world, (xd+100, yd-50))
            if direction == "Left":
                screen.blit(current_frame_the_world, (xd-150, yd-50))

        #I added the screen blit to blit the character here, near the end, as many changes are done above and it is best to put the blit command here.
        screen.blit(current_frame, (xd, yd))
        
        
        #Sets up a health bar for the enemy/object
        Enemy_Life()
        
        #Display update and FPS Clock
        pygame.display.update()
        fpsClock.tick(FPS)

        #Returns user to Main Menu once the health bar is empty
        if enemy_life == -500:
            MainMenu = True
            MainGame = False
            StandReveal = False

                                     

