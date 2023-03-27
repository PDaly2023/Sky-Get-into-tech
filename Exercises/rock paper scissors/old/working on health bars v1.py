import pygame
import sys
from button import Button
import random
from pygame import mixer

class Main_logic:
    def __init__(self):
        self.p2_choices = ('rock', 'paper', 'scissors')
        
    def p2_choice(self):
        
        self.choice = ''
        self.p2_choice = random.choice(self.p2_choices)
        return (self.p2_choice)
               
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
        print('player one has: ',p1_health,' lives left')
        print('player two has: ',p2_health,' lives left')
        return(p1_health, p2_health, draw)
    
class Scaling:
    def __init__(self):
        self.scalfactor = 1
        
    def best_of_scale(self, best_of):
        self.best_of = best_of
        print('Game now set to best of', self.best_of,'rounds')
        return(self.best_of)
    
# initialize game engine
pygame.init()

#Instantiate mixer
mixer.init()
#Set preferred volume
mixer.music.set_volume(0.5)

pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound/Fight.mp3'), maxtime=600)

#set screen size and initilise window
window_width=1280
window_height=720
size = (window_width, window_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
animation_increment=10
clock_tick_rate=20
best_of = 3


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
title = pygame.image.load("graphics/title.png").convert()
pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound/The World Warrior.mp3'), loops=-1)

#rects
rock_button_rect = rock_button_image.get_rect(topleft =(300, 600))
paper_button_rect = paper_button_image.get_rect(topleft =(535, 600))
scissors_button_rect = scissors_button_image.get_rect(topleft =(770, 600))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    print('best of ',best_of,'rounds set globally')
    while True:
        screen.blit(title, (0, 0))
        #Set preferred volume
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(160, 630), 
                            text_input="PLAY", font=get_font(75), base_color="#F6780A", hovering_color="White")
        options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(644, 630), 
                            text_input="OPTIONS", font=get_font(75), base_color="#F6780A", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1120, 630), 
                            text_input="QUIT", font=get_font(75), base_color="#F6780A", hovering_color="White")

        #screen.blit(MENU_TEXT, MENU_RECT)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(MENU_MOUSE_POS):
                    #Set preferred volume
                    mixer.music.set_volume(0.5)

                    #Load audio file
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound/Fight.mp3'), maxtime=600)
                    play()
                if options_button.checkForInput(MENU_MOUSE_POS):
                    options()
                if quit_button.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            
        pygame.display.update()
    

def options():
    while True:
        global best_of
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("white")
        options_text_1 = get_font(35).render("Press 1 for Best of 3", True, "Black")
        options_text_2 = get_font(35).render("Press 2 for Best of 5", True, "Black")
        options_text_3 = get_font(35).render("Press 3 for Best of 7", True, "Black")
        
        options_rect_1 = options_text_1.get_rect(center=(640, 250))
        options_rect_2 = options_text_1.get_rect(center=(640, 300))
        options_rect_3 = options_text_1.get_rect(center=(640, 350))

        screen.blit(options_text_1, options_rect_1)
        screen.blit(options_text_2, options_rect_2)
        screen.blit(options_text_3, options_rect_3)
        
        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    rounds = Scaling()
                    best_of = rounds.best_of_scale(3)
                    
                    
                if event.key == pygame.K_2:
                    rounds = Scaling()
                    best_of = rounds.best_of_scale(5)
                                        
                if event.key == pygame.K_3:
                    rounds = Scaling()
                    best_of = rounds.best_of_scale(7)
                    
        pygame.display.update()
    
                
        
        
        

#GAME LOOP
def play():
    game_active = True
    draw = 0
    if best_of == 3:
        p1_health = 2
        p1_starting_health = 2
        p2_health = 2
        p2_starting_health = 2
    elif best_of == 5:
        p1_health = 3
        p1_starting_health = 3
        p2_health = 3
        p2_starting_health = 3
    elif best_of == 7:
        p1_health = 5
        p1_starting_health = 5
        p2_health = 5
        p2_starting_health = 5
    action_taken = 0
    dead=False
    finished_game = 0
    p2_choice = ''
    wins = 0
    p2_wins = 0

        
# Draw health bars the old way
#    def draw_health_bars():
#            #DRAW HEALTH BARS
#        if p1_health == 2:
#            screen.blit(fullhealth_image, [217, 26])
#        if p1_health == 1:
#            screen.blit(p1_half_health_image, [217, 26])
#        if p1_health == 0:
#            screen.blit(empty_health_image, [217, 26])
#            
#
#            
#        if p2_health == 2:
#            screen.blit(fullhealth_image, [684, 26])
#        if p2_health == 1:
#            screen.blit(p2_half_health_image, [684, 26])
#        if p2_health == 0:
#            screen.blit(empty_health_image, [684, 26]) 

    def draw_health_bar_p1(pos, size, borderC, barC):
        progress = 1
        if p1_starting_health == 5:
            if p1_health == 5:
                progress = progress
            elif p1_health == 4:
                progress = progress - (progress /p1_starting_health)
            elif p1_health == 3:
                progress = progress - (progress /p1_starting_health) * 2
            elif p1_health == 2:
                progress = progress - (progress /p1_starting_health) * 3
            elif p1_health == 1:
                progress = progress - (progress /p1_starting_health) * 4
            elif p1_health == 0:
                progress = 0
        if p1_starting_health == 3:
            if p1_health == 3:
                progress = progress
            elif p1_health == 2:
                progress = progress - (progress /p1_starting_health) 
            elif p1_health == 1:
                progress = progress - (progress /p1_starting_health) * 2
            elif p1_health == 0:
                progress = 0
        if p1_starting_health == 2:
            if p1_health == 2:
                progress = progress
            elif p1_health == 1:
                progress = progress - (progress /p1_starting_health) 
            elif p1_health == 0:
                progress = 0
        pygame.draw.rect(screen, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, pos[1]+3)
        innerSize = ((size[0]-6) * progress, size[1]-6)
        pygame.draw.rect(screen, barC, (*innerPos, *innerSize))
        
        
    def draw_health_bar_p2(pos, size, borderC, barC):
        progress = 1
        if p2_starting_health == 5:
            if p2_health == 5:
                progress = progress
            elif p2_health == 4:
                progress = progress - (progress /p2_starting_health)
            elif p2_health == 3:
                progress = progress - (progress /p2_starting_health) * 2
            elif p2_health == 2:
                progress = progress - (progress /p2_starting_health) * 3
            elif p2_health == 1:
                progress = progress - (progress /p2_starting_health) * 4
            elif p2_health == 0:
                progress = 0
        if p2_starting_health == 3:
            if p2_health == 3:
                progress = progress
            elif p2_health == 2:
                progress = progress - (progress /p2_starting_health) 
            elif p2_health == 1:
                progress = progress - (progress /p2_starting_health) * 2
            elif p2_health == 0:
                progress = 0
        if p2_starting_health == 2:
            if p2_health == 2:
                progress = progress
            elif p2_health == 1:
                progress = progress - (progress /p2_starting_health) 
            elif p2_health == 0:
                progress = 0
        pygame.draw.rect(screen, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, pos[1]+3)
        innerSize = ((size[0]-6) * progress, size[1]-6)
        pygame.draw.rect(screen, barC, (*innerPos, *innerSize))


    def draw_overlay(finished_game):
            #P1 WINS
            
            if p2_health == 0:
                screen.blit(gameover_image, [359, 190])
                #pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound/you_win.mp3'))
                finished_game = 1
                return(finished_game)
                
            #P1 LOSES
            if p1_health == 0:
                screen.blit(gameover2_image, [359, 190])
                #pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound/you_lose.mp3'))
                finished_game = 1
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
                
   
    while(dead==False):
        pygame.display.set_caption("Super Rock Paper Scissors Turbo")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.mixer.Channel(1).pause()
                dead = True
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #if mouse is touching rock_button_rect and mouse button is pressed , set choice
                    if rock_button_rect.collidepoint(event.pos):
                        if p1_health != 0 and p2_health != 0:
                            draw = 0
                            chosen = 'rock'
                            p1_choice = Main_logic()
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
                        if p2_health == 0:
                            wins += 1
                        else:
                            p2_wins += 1
                        action_taken = 0
                        finished_game = 0
                        if best_of == 3:
                            p1_health = 2
                            p2_health = 2
                            
                        elif best_of == 5:
                            p1_health = 3
                            p2_health = 3

                        elif best_of == 7:
                            p1_health = 5
                            p2_health = 5
                        print('player 1 health reset to:',p1_health)
                        print('player 2 health reset to:',p2_health)
                        
        if game_active:
            
            #DRAW BACKGROUNDIMAGE
            screen.blit(background_image, [0, 0])
            #DRAW HEALTHFRAME
            screen.blit(healthframe_image, [214, 15])

            #DRAW BUTTONS FOR PLAYER CHOICES
            screen.blit(rock_button_image, [300, 600])
            screen.blit(paper_button_image, [535, 600])
            screen.blit(scissors_button_image, [770, 600])



# testing new health bars

            barPos = (217, 26)
            barPos_p2 = (684, 26)
            barSize = (379, 27)
            borderColor = (0, 0, 0)
            barColor = (0, 128, 0) 
            draw_health_bar_p1(barPos,barSize,borderColor,barColor)
            draw_health_bar_p2(barPos_p2,barSize,borderColor,barColor)
            
            #draw_health_bar
            #draw_health_bars()


            #draw_sprites
            draw_sprites()
        
            #display overall wins/losses
            pygame.font.init()
            my_font = pygame.font.Font('font/Pixeltype.ttf', 50)
            total_wins = 'Wins: ' +str(wins)
            p2_total_wins = 'Wins: ' +str(p2_wins)
                                          
            wins_surface = my_font.render(total_wins, False, (0, 0, 0))
            p2_wins_surface = my_font.render(p2_total_wins, False, (0, 0, 0))
            screen.blit(wins_surface, (214,60))
            screen.blit(p2_wins_surface, (960,60))
                                          
            finished_game = draw_overlay(finished_game)

            pygame.display.update()   
            #pygame.display.flip()
            clock.tick(clock_tick_rate)
            

main_menu()
