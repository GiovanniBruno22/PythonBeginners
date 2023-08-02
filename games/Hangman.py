import random

# simple terminal hangman game with ASCII art
def choose_random_word():
    word_list = ["hangman", "python", "programming", "developer", "challenge", "knowledge"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def draw_hangman(attempts):
    hangman_stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """
    ]
    
    print(hangman_stages[attempts])

def hangman():
    word_to_guess = choose_random_word()
    max_attempts = len(word_to_guess) + 2
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word_to_guess:
            attempts += 1
            draw_hangman(attempts)
        
        print(display_word(word_to_guess, guessed_letters))
        
        if '_' not in display_word(word_to_guess, guessed_letters):
            print("You won! You guessed the word:", word_to_guess)
            break
        
        if attempts >= max_attempts:
            print("Sorry, you lost. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()