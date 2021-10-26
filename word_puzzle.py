"""
------------------------------------------------------------------------------------------------------------------------
Mini-Project Word Puzzle
In the Word Puzzle program, user will trying to guess a secret word. For user , each time they need to input a
letter. There are four chances in total. If the user guesses a letter that isn't a part of the secret word or a
letter already been guessed, the user will lose a chance. If the user guesses a letter that is part of the secret
word and haven't been guessed, occurrences of this letter in the secret word will be displayed in the right position
and user won't loss a chance. The program will end when user guessed all letter in the secret word or user used all
their four chances.
------------------------------------------------------------------------------------------------------------------------
"""

import random


# Display instructions.
def display_instructions():
    instructions_file = open('wp_instructions.txt', 'r')
    instructions = instructions_file.read()
    instructions_file.close()
    print(instructions)


# Display the current puzzle state.
def current_puzzle_state(guess_list):
    print('The answer so far is', ' '.join(guess_list))


# Running the main game loop. In this user-defined function, it calls two other user-defined functions.
def main_game_loop(guess_list, secret_word):
    empty = True  # record if there is any '_' in the 'guess_list'
    chances = 4  # the four chances to make a mistake
    all_input = []  # all the user inputs

    # If user haven't guessed the whole word and they haven't used up their four chances, the program will continuing
    # running.
    while empty and chances > 0:
        current_puzzle_state(guess_list)
        need_plus = update_puzzle_state(chances, guess_list, secret_word, all_input)
        empty = '_' in guess_list

        # Subtract one chance each time, if the guess is correct, add that chance back.
        chances -= 1
        if need_plus:
            chances += 1

    current_puzzle_state(guess_list)  # show the final state


# update the puzzle state after a guess
def update_puzzle_state(chances, guess_list, secret_word, all_input):
    changed = False  # record if 'guess_list' change after an update
    guess = input('Guess a letter (' + str(chances) + ' guesses remaining): ')
    all_input.append(guess)

    # Compare the latest input with all previous inputs. If there is repetition, this input can't be correct.
    for i in range(len(all_input) - 1):
        if all_input[-1] == all_input[i]:
            changed = False
            return changed

    # Searching every characters in the secret word, it will updating the corresponding positions in 'guess_list' to
    # user input and change 'changed' to 'True'. If no action takes, 'changed' remaining as 'False'.
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            guess_list[i] = guess
            changed = True

    return changed


# display results
def display_results(guess_list, secret_word):
    # Using '_' as the key to identify whether user guessed the whole word.
    if '_' in guess_list:
        print('Not quite, the correct word was ' + secret_word + '. Better luck next time')
    else:
        print('Good job! You found the word ' + secret_word + '!')

    end = input('Press enter to end the game. ')


def main():
    list_of_words = ('apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango')
    secret_word = random.choice(list_of_words)  # randomly chose a word

    # The guess list which user will putting their correct guess in it.
    guess_list = list()
    for i in secret_word:
        guess_list.append('_')

    display_instructions()  # show the instructions, the beginning of the program
    main_game_loop(guess_list, secret_word)  # the main part of the program
    display_results(guess_list, secret_word)  # show results, the end of the program


main()
