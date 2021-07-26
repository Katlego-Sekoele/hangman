import random

LINE = "===================================================="
hangman_drawing = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
file_length_hard = 60823
file_length_normal = 850

#NEw comment

def get_word_from_lexicon(difficulty):
    """Returns the list version of a word from one of two lexicons. Example, the word donkey will be returned as ['d', 'o', 'n', 'k', 'e', 'y']"""
    try:
        if difficulty == "normal":
            line_number = random.randint(1, file_length_normal) 
        else:
            line_number = random.randint(1, file_length_hard)
        word = open("{}.txt".format(difficulty), "r").readlines()[line_number]
        return list(word[:-1])
    except Exception as e:
        print(e)


def censored_word_list(word):
    """Creates a censored list. A list of the same length as the word list"""
    word_censored_list = []
    for i in range(len(word)):
        word_censored_list.append("_")
    return word_censored_list


def draw_hangman(part_number):
    """Prints a body part of the hangman figure"""
    print(hangman_drawing[part_number])


def reveal_letter(word, word_censored, letter_to_reveal):
    """Reveals a letter or multiple letters from the censored list"""
    for i in range(len(word)):
        if word[i] == letter_to_reveal:
            word_censored[i] = letter_to_reveal
    return word_censored


def guess_letter(word, word_censored, letter, part_number):
    """Determines whether or not a letter must be revealed or if a body part must be revealed"""
    if letter in word:
        return reveal_letter(word, word_censored, letter)
    else:
        draw_hangman(part_number)
        return part_number + 1


def initialise_game():
    """Sets the initial conditions of the game"""
    difficulty_input = input(LINE + "\nPlease select a difficulty:\n1. Normal\n2. Hard\n--> ")
    difficulty = "normal" if difficulty_input == "1" else "hard"
    word = get_word_from_lexicon(difficulty)
    censored_word = censored_word_list(word)
    game(word, censored_word)


def game(word, censored_word):
    """Handles the game logic"""
    # print(word)
    start_game = int(input(LINE + "\nMenu:\n1. Start game\n0. Quit\n--> "))
    if start_game == 1:
        part_number = 0
        past_guesses = []
        print(LINE + "\n" + " ".join(censored_word))
        while part_number < len(hangman_drawing):
            user_guess = input("Guess a letter:\n--> ")
            while user_guess in past_guesses or len(user_guess) != 1:
                user_guess = input("Guess a letter:\n--> ")
            past_guesses.append(user_guess)
            if user_guess in word:
                censored_word = guess_letter(word, censored_word, user_guess, part_number)
                print(LINE + "\n" + " ".join(censored_word))
            else:
                part_number = guess_letter(word, censored_word, user_guess, part_number)
                print(LINE + "\n" + " ".join(censored_word))
            if "_" not in censored_word:
                print("CONGRATULATIONS!! You found the correct word")
                break
        else:
            print("You unfortunately lost, the word was {}".format("".join(word)))
    else:
        print("Have a great day, goodbye")


if __name__ == '__main__':
    initialise_game()

# TODO: Clean up code, clean up outputs, error handling
