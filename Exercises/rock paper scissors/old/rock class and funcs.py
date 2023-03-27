import pygame
import random
from pygame import mixer

class Main_logic:
    def __init__(self):
        self.p2_choices = ('rock', 'paper', 'scissors')
        
    def p2_choice(self):
        
        self.choice = ''
        self.p2_choice = random.choice(self.p2_choices)
        return (self.p2_choice)
    
#    def sprite(self, chosen):
#        
#        self.choice = chosen
#        if self.choice == 'rock':
#            print('player chose rock!')
#        if self.choice == 'paper':
#            print('player chose paper!')         
#        if self.choice == 'scissors':
#            print('player chose scissors!')
            
    def logic(self, chosen, p1_health, p2_health, draw):
        self.choice = chosen
        p1_health = p1_health
        p2_health = p2_health
        draw = draw
        print('current p2 choice is',self.p2_choice)
        print ('current p1 choice is', self.choice)
        
        if self.choice == self.p2_choice:
            print('DRAWN GAME')
            draw = 1
        elif self.choice == 'rock' and self.p2_choice == 'scissors':
            print('you win')
            p2_health -= 1
        elif self.choice == 'paper' and self.p2_choice == 'rock':
            print('you win')
            p2_health -= 1
        elif self.choice == 'scissors' and self.p2_choice == 'paper':
            print('you win')
            p2_health -= 1
        else:
            print('you lose')
            p1_health -= 1    
        return(p1_health, p2_health, draw)


def draw_health_bars():
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


def draw_overlay(finished_game):
            #P1 WINS
        if p2_health == 0:
            screen.blit(gameover_image, [359, 190])
            print('YOU WIN!!!! - GAME OVER')
            finished_game = 1
            return(finished_game)
            
        #P1 LOSES
        if p1_health == 0:
            screen.blit(gameover2_image, [359, 190])
            finished_game = 1
            print('YOU LOSE - GAME OVER')
            return(finished_game)


        #If DRAW
        if draw == 1:
            screen.blit(drawgame_image, [500, 165])

def draw_sprites():
    #draw player sprites
    if action_taken == 1:
        screen.blit(p1_draw, [217, 300])
        if p2_choice == 'rock':
            screen.blit(rock_image_flip, [747, 300])
        if p2_choice == 'paper':
            screen.blit(paper_image_flip, [747, 300])
        if p2_choice == 'scissors':
            screen.blit(scissors_image_flip, [747, 300])
            
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

#set screen size and initilise window
window_width=1280
window_height=720
size = (window_width, window_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Rock Paper Scissors Turbo")
game_active = True
draw = 0
p1_health = 2
p2_health = 2
action_taken = 0
animation_increment=10
clock_tick_rate=20
dead=False
finished_game = 0
p2_choice = ''
clock = pygame.time.Clock()

#load images
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

#rects
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
                    if p1_health != 0 and p2_health != 0:
                        draw = 0
                        chosen = 'rock'
                        p1_choice = Main_logic()
                        #p1_choice.sprite(chosen)
                        p2_choice = p1_choice.p2_choice()
                        p1_health, p2_health, draw = p1_choice.logic(chosen, p1_health, p2_health, draw)
                        action_taken = 1
                        p2_draw = p2_choice
                        p1_draw = rock_image

                #if mouse is touching paper_button_rect and mouse button is pressed , set choice
                if paper_button_rect.collidepoint(event.pos):
                    if p1_health != 0 and p2_health != 0:
                        draw = 0
                        chosen = 'paper'
                        p1_choice = Main_logic()
                        #p1_choice.sprite(chosen)
                        p2_choice = p1_choice.p2_choice()
                        p1_health, p2_health, draw = p1_choice.logic(chosen, p1_health, p2_health, draw)
                        action_taken = 1
                        p2_draw = p2_choice
                        p1_draw = paper_image
                    
                #if mouse is touching scissors_button_rect and mouse button is pressed , set choice
                if scissors_button_rect.collidepoint(event.pos):
                    draw = 0
                    if p1_health != 0 and p2_health != 0:
                        chosen = 'scissors'
                        p1_choice = Main_logic()
                        #p1_choice.sprite(chosen)
                        p2_choice = p1_choice.p2_choice()
                        p1_health, p2_health, draw = p1_choice.logic(chosen, p1_health, p2_health, draw)
                        action_taken = 1
                        p2_draw = p2_choice
                        p1_draw = scissors_image

                    
        elif event.type == pygame.KEYDOWN:
            #if space button is pressed
            if event.key == pygame.K_SPACE:
                if finished_game == 1:
                    print('restarting game!')
                    action_taken = 0
                    finished_game = 0
                    #p1_choice.sprite('blank')
                    p1_health = 2
                    p2_health = 2
    if game_active:
        
    #DRAW BACKGROUNDIMAGE
        screen.blit(background_image, [0, 0])
        #DRAW HEALTHFRAME
        screen.blit(healthframe_image, [214, 15])

        #DRAW BUTTONS FOR PLAYER CHOICES
        screen.blit(rock_button_image, [300, 600])
        screen.blit(paper_button_image, [535, 600])
        screen.blit(scissors_button_image, [770, 600])

        
                
        #draw health bars       
        draw_health_bars()

        #draw_sprites
        draw_sprites()
        
        #draw_game_overlay
        finished_game = draw_overlay(finished_game)

            
        pygame.display.flip()
        clock.tick(clock_tick_rate)
