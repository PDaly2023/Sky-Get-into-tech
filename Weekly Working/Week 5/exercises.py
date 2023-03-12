from collections import Counter

#Question 1
def cels_to_fahr(celcius):
    fahr =((9 * celcius) / 5) + 32
    return fahr


print(cels_to_fahr(-5))
print(cels_to_fahr(30))
print(cels_to_fahr(100))

print('\n')

#Question 2
def multip_tables(number, maximum=12):

    for i in range(1,maximum+1):
        print(number * i)
    return


num_choice = input('Please input the number you would like to see the multiplication table for:')
multip_tables(int(num_choice))

#Question 3
def average_number(numbers_list, average_type = 2):
    if average_type == 1: #mean:
        # all numbers added together, divided by number of elements
        result = 0
        for i in numbers_list:
            result += int(i)
        print('The sum of the input numbers is:', result)
        mean = result / len(numbers_list)
        print('The mean average of the input numbers is:', mean)

    if average_type == 2: #mode:
        # The most commonly occuring value
        count = dict(Counter(numbers_list))
        print('The modal average of the input numbers is:', max(count, key=count.get))


    if average_type == 3: #median:
        # Place all values in order, smallest to highest. find the one in the middle
        numbers_list.sort()
        if len(numbers_list) %2 == 0:
            middle_number = int(len(numbers_list) / 2)
            left_middle = int(numbers_list[middle_number-1])
            right_middle = int(numbers_list[middle_number])
            median = (left_middle + right_middle) / 2
            print('the median value of the numbers given is:', median)

        else:
            middle_number = int((len(numbers_list) +1) / 2)
            median = (numbers_list[middle_number-1])
            print('the median value of the numbers given is:', median)
    return


print('\n')

av_type = input('''Which Average type would you like?
1. Mean
2. Mode
3. Median\n''')

numbers_chosen = (input('Please add your numbers separated by a comma:'))
numbers_list = numbers_chosen.split(',')

average_number(numbers_list, int(av_type))

#Question 4
#Find palindromic numbers within a given range
#CHRIS'S ANSWER

def palindromic_numbers_in_range(*, start=1, stop=100):
    # Guard clauses to ensure we have values that we can work with
    # Check both our values are integers
    if type(start) != int or type(stop) != int:
        return None
    # Check we're not meant to stop before we've started
    elif stop < start:
        return None

    # Create an empty set
    palindromic_numbers = set()

    # Iterate through our range
    for i in range(start, stop + 1):
        # If the stringified version of i equal to the reverse of stringified then add i to our set
        # We're using the defaults for the first 2 values of our slice to get the entire string
        # and then setting the 3rd value of our slice, known as the step, to -1 to reverse it
        if str(i) == str(i)[::-1]:
            palindromic_numbers.add(i)

    return palindromic_numbers


# Find our palindromic numbers in various ranges
print(palindromic_numbers_in_range())
print(palindromic_numbers_in_range(start=3000, stop=4000))
print(palindromic_numbers_in_range(start=12030, stop=194000))

# Test some edge cases
print(palindromic_numbers_in_range(start=-5, stop=-1))
print(palindromic_numbers_in_range(start=12, stop=21))
print(palindromic_numbers_in_range(start=22, stop=20))
print(palindromic_numbers_in_range(start='a', stop=[]))


#Question 5
#Create a guess the word game (computer knows the word, player has to guess)
#CHRIS'S ANSWER

# 5. Create a guess the word game (computer knows the word, player has to guess)

# Define some constants. A constant is a variable whose value never changes
# In Python, we define constants with an upper case variable name as below
COMPUTER_WORD = 'derelict'
CLUES = [
    f'It has {len(COMPUTER_WORD)} letters',
    'It rhymes with clicked',
    'A synonym is abandoned',
    'It starts with d'
]

# Set our possible clue frequency values
EASY = 1
MEDIUM = 2
HARD = 3
IMPOSSIBLE = 0

# Put those clue frequencies in a list ordered by difficulty
DIFFICULTIES = [EASY, MEDIUM, HARD, IMPOSSIBLE]


def is_the_computer_word(word):
    # ensure that we use .lower to be case-insensitive
    return word.lower() == COMPUTER_WORD.lower()


def letters_in_common(word):
    # Create a list with an underscore for each letter of the computer word
    letters = ['_'] * len(COMPUTER_WORD)

    # Enumerate over our given word but only up to the length of the computer word
    for i, letter in enumerate(word[:len(COMPUTER_WORD)]):
        # If the letter at index i is the same as our letter then update our list with that letter
        if COMPUTER_WORD[i] == letter.lower():
            letters[i] = letter

    # Return a string of our letters rather than a list
    return "".join(letters)


def should_print_clue(iteration_number, clue_frequency):
    # If we're on impossible difficulty, don't give any clues
    if clue_frequency == IMPOSSIBLE:
        return False
    # Otherwise, return a clue only every clue_frequency iterations
    return iteration_number % clue_frequency == 0


def print_clue(num_clues_given):
    # Check whether we have any other clues left
    if num_clues_given >= len(CLUES):
        # Notice the escaped apostrophe
        print('I\'m all out of ideas for clues, sorry!')
        return
    # If we have clues left, print a clue out with an f string using num_clues_given as the index of the clue
    print(f'Clue: {CLUES[num_clues_given]}')


def is_valid_difficulty(difficulty):
    # Make sure we have a number and that it is between 0 and 4
    return difficulty.isnumeric() and int(difficulty) in list(range(0, len(DIFFICULTIES)))


def get_clue_frequency_string(chosen_clue_frequency):
    # Get a nicely formatted string to tell the player how often they will get a clue
    # Could have used match case pattern matching here but opted for standard if, elif, else
    if chosen_clue_frequency == IMPOSSIBLE:
        clue_frequency_string = 'No clues for you!'
    elif chosen_clue_frequency == EASY:
        clue_frequency_string = 'You\'ll get a clue every turn'
    elif chosen_clue_frequency == MEDIUM:
        clue_frequency_string = 'You\'ll get a clue every other turn'
    else:
        clue_frequency_string = f'You\'ll get a clue every {chosen_clue_frequency} turns'

    return clue_frequency_string


def select_difficulty():
    # Keep looping until player chooses a valid difficulty and then return that
    while True:
        # Have to be len(DIFFICULTIES) - 1 as we are counting from 0
        difficulty = input(f'Select your difficulty from 0 to {len(DIFFICULTIES) - 1}: ')
        if is_valid_difficulty(difficulty):
            # Look up the clue frequency in our DIFFICULTIES list that is a constant
            chosen_clue_frequency = DIFFICULTIES[int(difficulty)]
            print(f'You chose a difficulty level of {difficulty}.', get_clue_frequency_string(chosen_clue_frequency))
            # We return here so that we immediately leave the function which therefore terminates our loop
            return chosen_clue_frequency
        print(f'Please choose a number between 0 and {len(DIFFICULTIES) - 1}.')


def game_loop(clue_frequency):
    # Run our game with the clue_frequency having been pre-selected
    clues_given = 0
    iteration = 0

    # Loop forever (or until we hit a break)
    while True:
        # If we should give a clue then give it before the first guess
        if should_print_clue(iteration, clue_frequency):
            print_clue(clues_given)
            clues_given += 1

        # Check if the player has input the correct value and break out of our loop if so
        player_word = input(f'What do you think my word is? ')
        if is_the_computer_word(player_word):
            print('You got it!')
            break

        # Otherwise, print out our string showing what is correct or not
        print(f'Not quite, you have the following letters correct: {letters_in_common(player_word)}')


# A function named main is the traditional place where, as the name implies, the main functionality should occur
def main():
    # Loop forever or until we hit a break statement
    while True:
        print('Let\'s play a game. Guess the word I\'m thinking of....')

        # Set a difficulty and then run a game with that chosen difficulty
        clue_frequency = select_difficulty()
        game_loop(clue_frequency)

        # Has the player had enough? If so call it a day
        if input('Want to play again? Y/N (default Y): ').upper() == 'N':
            print('Thanks for playing')
            break


# This conditional means that we will only run our code if this file is ran as a script
# If another python file imports this file as a module, the game will not run unless explicitly called
if __name__ == "__main__":
    main()
