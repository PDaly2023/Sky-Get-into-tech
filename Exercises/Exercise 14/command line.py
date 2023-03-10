
import random

#intiialise p1_choice and p2_choice
player_choice = None
p1_score = 0
p2_score =0
cpu_choice = None
choices = ('rock', 'paper', 'scissors')
dict_choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}


leave = False

def process_choices(p1_choice,p2_choice,p1_score,p2_score):
    #P1 CHOSE ROCK
    if p1_choice == 'rock':
        print('player chose rock')
        print('cpu chose', p2_choice)
        if p1_choice == p2_choice:
            print('It\'s a draw!\n')
            draw = 1
        if p2_choice == 'paper':
            print('you lose!\n')
            p2_score += 1
        if p2_choice == 'scissors':
            print('you win!\n')
            p1_score += 1
        p1_choice = None
        
        
        
    #P1 CHOSE PAPER
    elif p1_choice == 'paper':    
        print('player chose paper')
        print('cpu chose', p2_choice)
        if p1_choice == p2_choice:
            print('It\'s a draw!\n')
            draw = 1
        if p2_choice == 'scissors':
            print('you lose!\n')
            p2_score += 1
        if p2_choice == 'rock':
            print('you win!\n')
            p1_score += 1
        p1_choice = None
       


    #P1 CHOSE SCISSORS
    elif p1_choice == 'scissors': 
        print('player chose scissors')
        print('cpu chose', p2_choice)
        if p1_choice == p2_choice:
            print('It\'s a draw!\n')
        if p2_choice == 'rock':
            print('you lose!\n')
            p2_score += 1
        if p2_choice == 'paper':
            print('you win!\n')
            p1_score += 1
        p1_choice = None

    else:
        print('I can only accept the following inputs: Rock, paper or scissors\n')

    return(p1_score,p2_score)


def convert_letter_to_word(letter):
    value = None
    if len(letter) != 1:
        letter = letter[0]
    if len(letter) == 1:
        search_key = letter
        value = [val for key, val in dict_choices.items() if search_key in key]
        return(value[0])
                
        

while leave == False:        
    player_choice = input('Please choose Rock, Paper Or Scissors: (can be input as r, p, s) ').lower()
    player_choice = convert_letter_to_word(player_choice,)  
    cpu_choice_random = random.randint(0,2)
    cpu_choice = choices[cpu_choice_random]
    p1_score, p2_score = process_choices(player_choice, cpu_choice, p1_score, p2_score)
    print('player score =', p1_score)
    print('CPU score =', p2_score, '\n')
    if p1_score == 3:
        print('YOU WIN')
        break
    if p2_score == 3:
        print('YOU LOSE')
        break
    
    


    


