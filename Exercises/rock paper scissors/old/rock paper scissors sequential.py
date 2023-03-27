# import pygame
import pygame
import random
from pygame import mixer

# initialize game engine
pygame.init()

#Instantiate mixer
mixer.init()

#Set preferred volume
mixer.music.set_volume(0.5)

#Load audio file
mixer.music.load('sound/The World Warrior.mp3')

#Set preferred volume
mixer.music.set_volume(0.5)

#Play the music
mixer.music.play(loops = -1)

window_width=1280
window_height=720

#intiialise p1_choice and p2_choice
p1_choice = None
p2_choice = None
p2_choices = ('rock', 'paper', 'scissors')
draw = 0

#P1 AND p2 HEALTH VALUES
p1_health = 2
p2_health = 2

finished_game = 0

p1_draw = None

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Super Rock Paper Scissors Turbo")



dead=False

clock = pygame.time.Clock()

#LOAD ALL IMAGES
background_image = pygame.image.load("graphics/background.PNG").convert_alpha()
background_image = pygame.transform.scale(background_image, (1280, 720))
fullhealth_image = pygame.image.load("graphics/fullhealth.bmp").convert()
healthframe_image = pygame.image.load("graphics/healthbarframe.PNG").convert_alpha()
p1_half_health_image = pygame.image.load("graphics/p1halfhealth.bmp").convert()
p2_half_health_image = pygame.image.load("graphics/p2halfhealth.bmp").convert()
empty_health_image = pygame.image.load("graphics/emptyhealth.bmp").convert()
rock_image = pygame.image.load("graphics/rock.PNG").convert_alpha()
rock_image = pygame.transform.scale(rock_image, (320, 180))
rock_image_flip = pygame.transform.flip(rock_image, True, False)
paper_image = pygame.image.load("graphics/paper.PNG").convert_alpha()
paper_image = pygame.transform.scale(paper_image, (320, 180))
paper_image_flip = pygame.transform.flip(paper_image, True, False)
scissors_image = pygame.image.load("graphics/scissors.PNG").convert_alpha()
scissors_image = pygame.transform.scale(scissors_image, (320, 180))
scissors_image_flip = pygame.transform.flip(scissors_image, True, False)
drawgame_image = pygame.image.load("graphics/drawgame.PNG").convert_alpha()
gameover_image = pygame.image.load("graphics/gameover.PNG").convert_alpha()
gameover2_image = pygame.image.load("graphics/gameover2.PNG").convert_alpha()
rock_button_image = pygame.image.load("graphics/rockbutton.png").convert()
paper_button_image = pygame.image.load("graphics/paperbutton.png").convert()
scissors_button_image = pygame.image.load("graphics/scissorsbutton.png").convert()

#CREATE BUTTONS RECTANGLES
#using get_rect method to match image size
rock_button_rect = rock_button_image.get_rect(topleft =(300, 600))
paper_button_rect = paper_button_image.get_rect(topleft =(535, 600))
scissors_button_rect = scissors_button_image.get_rect(topleft =(770, 600))

#GAME LOOP
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #if mouse is touching rock_button_rect and mouse button is pressed , set choice
                if rock_button_rect.collidepoint(event.pos):
                    p1_choice = 'rock'

                #if mouse is touching paper_button_rect and mouse button is pressed , set choice
                if paper_button_rect.collidepoint(event.pos):
                    p1_choice = 'paper'
                
                #if mouse is touching scissors_button_rect and mouse button is pressed , set choice
                if scissors_button_rect.collidepoint(event.pos):
                    p1_choice = 'scissors'
        elif event.type == pygame.KEYDOWN:
            #if space button is pressed
            if event.key == pygame.K_SPACE:
                if finished_game == 1:
                    print('restarting game!')
                    p1_choice = None
                    p2_choice = None
                    finished_game = 0
                    p1_draw = None
                    p1_health = 2
                    p2_health = 2
                

                
                #'''check if mouse if over player rectangle'''
                #if event.type == pygame.MOUSEMOTION:
                #   if scissors_button_rect.collidepoint(event.pos): print('collision')                  
            

    #DRAW BACKGROUNDIMAGE
    screen.blit(background_image, [0, 0])
    #DRAW HEALTHFRAME
    screen.blit(healthframe_image, [214, 15])

    #DRAW BUTTONS FOR PLAYER CHOICES
    screen.blit(rock_button_image, [300, 600])
    screen.blit(paper_button_image, [535, 600])
    screen.blit(scissors_button_image, [770, 600])
                        

    
    #P1 AND P2 CHOICE VALUES
    #P1 CHOSE ROCK
    if p1_choice == 'rock' and p1_health != 0 and p2_health != 0:
        draw = 0
        print('player chose rock!')
        print('p1_choice = ', p1_choice)
        p1_draw = 'rock'
        p2_choice = random.choice(p2_choices)
        print('p2_choice = ', p2_choice)
        if p1_choice == p2_choice:
            print('DRAW GAME')
            draw = 1
        if p2_choice == 'paper':
            print('you lose!')
            p1_health = p1_health - 1
        if p2_choice == 'scissors':
            print('you win!')
            p2_health = p2_health - 1
        p1_choice = None
        
        
        
    #P1 CHOSE PAPER
    if p1_choice == 'paper' and p1_health != 0 and p2_health != 0:    
        draw = 0
        print('player chose paper!')
        print('p1_choice = ', p1_choice)
        p1_draw = 'paper'
        p2_choice = random.choice(p2_choices)
        print('p2_choice = ', p2_choice)
        if p1_choice == p2_choice:
            print('DRAW GAME')
            draw = 1
        if p2_choice == 'scissors':
            print('you lose!')
            p1_health = p1_health - 1
        if p2_choice == 'rock':
            print('you win!')
            p2_health = p2_health - 1
        p1_choice = None
       


    #P1 CHOSE SCISSORS
    if p1_choice == 'scissors' and p1_health != 0 and p2_health != 0: 
        draw = 0
        print('player chose scissors!')
        print('p1_choice = ', p1_choice)
        p1_draw = 'scissors'
        p2_choice = random.choice(p2_choices)
        print('p2_choice = ', p2_choice)
        if p1_choice == p2_choice:
            print('DRAW GAME')
            draw = 1
        if p2_choice == 'rock':
            print('you lose!')
            p1_health = p1_health - 1
        if p2_choice == 'paper':
            print('you win!')
            p2_health = p2_health - 1
        p1_choice = None
        

       
    #DRAW ROCK, PAPER, SCISSORS FOR P1
    if p1_draw == 'rock':
        screen.blit(rock_image, [217, 300])
    if p1_draw == 'paper':
        screen.blit(paper_image, [217, 300])
    if p1_draw == 'scissors':
        screen.blit(scissors_image, [217, 300])

    
    #DRAW ROCK, PAPER, SCISSORS FLIPPED HORIZONTALLY FOR P2
    if p2_choice == 'rock':
        screen.blit(rock_image_flip, [747, 300])
    if p2_choice == 'paper':
        screen.blit(paper_image_flip, [747, 300])
    if p2_choice == 'scissors':
        screen.blit(scissors_image_flip, [747, 300])


    #DRAW HEALTH BARS
    if p1_health == 2:
        screen.blit(fullhealth_image, [217, 26])
    if p1_health == 1:
        screen.blit(p1_half_health_image, [217, 26])
    if p1_health == 0:
        screen.blit(empty_health_image, [217, 26])

        
    if p2_health == 2:
        screen.blit(fullhealth_image, [684, 26])
    if p2_health == 1:
        screen.blit(p2_half_health_image, [684, 26])
    if p2_health == 0:
        screen.blit(empty_health_image, [684, 26])

    #P1 WINS
    if p2_health == 0:
        screen.blit(gameover_image, [359, 190])
        finished_game = 1
        print('YOU WIN!!!! - GAME OVER')
        
    #P1 LOSES
    if p1_health == 0:
        screen.blit(gameover2_image, [359, 190])
        finished_game = 1
        print('YOU LOSE - GAME OVER')


    #If DRAW
    if draw == 1:
        screen.blit(drawgame_image, [500, 165])

        
    pygame.display.flip()
    clock.tick(clock_tick_rate)
