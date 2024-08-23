import random
import datetime
# List of words for the game
words = {
    'easy': ['big', 'bus', 'sea', 'air'],
    'medium': ['fruits', 'cities', 'colors', 'places'],
    'hard': ['mongodb', 'javascript', 'python', 'java']
}
# Hangman figures
hangman = [
'''
_______
| |
|
|
|
|
_________|_
''',
'''
_______
| |
O |
|
|
|
_________|_
''',
'''
_______
| |
O |
| |
|
|
_________|_
''',
'''
_______
| |
O |
/| |
|
|
_________|_
''',
'''
_______
| |
O |
/|\\ |
|
|
_________|_
''',
'''
_______
| |
O |
/|\\ |
/ |
|
_________|_
''',
'''
_______
| |
O |
/|\\ |
/ \\ |
|
_________|_
'''
]
def select_word(difficulty):
    """Selects a random word from the words list based on the chosen difficulty."""
    word_list = words[difficulty]
    return random.choice(word_list)
def display_hangman(incorrect_guesses):
    """Displays the current hangman figure based on the number of incorrect guesses."""
    if incorrect_guesses < len(hangman):
        print(hangman[incorrect_guesses])
    else:
        print("Hangman figure not found.")
def play_hangman():
    print("Welcome to Text Hangman!")
    print("Choose a difficulty level: easy, medium, or hard")
    difficulty = input("Difficulty: ").lower()
    if difficulty not in words:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        return
    selected_word = select_word(difficulty)
    guessed_word = ['_'] * len(selected_word)
    remaining_guesses = 7
    guessed_letters = []
    start_time = datetime.datetime.now()
    print(f"You have chosen {difficulty} difficulty.")
    print("Guess the word by entering one letter at a time.")
    while '_' in guessed_word and remaining_guesses > 0:
        print("Word:", ' '.join(guessed_word))
        display_hangman(7 - remaining_guesses)
        print("Remaining Guesses:", remaining_guesses)
        guessed_letter = input("Enter a letter: ").lower()
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print("Please enter a single letter.")
            continue
        if guessed_letter in guessed_letters:
            print("You have already guessed that letter.")
            continue
        guessed_letters.append(guessed_letter)
        if guessed_letter in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == guessed_letter:
                    guessed_word[i] = guessed_letter
                else:
                    remaining_guesses -= 1
                    print("Incorrect guess. Try again!")
    end_time = datetime.datetime.now()
    game_duration = end_time - start_time
    if '_' not in guessed_word:
        print("Congratulations! You guessed the word:", ''.join(guessed_word))
        print("You win!")
    else:
        display_hangman(7)
        print("Sorry, you ran out of guesses.")
        print("The word was:", selected_word)
        print("You lose!")
        print("Game Duration:", game_duration)
def main():
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__" :
    main()