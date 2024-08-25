# Hangman-Game


A simple command-line Hangman game implemented in Python. Test your guessing skills by selecting a word from various difficulty levels and try to guess it before running out of guesses!

**Features**

Difficulty Levels: Choose between easy, medium, or hard.

Visual Hangman: Track your progress with dynamic hangman drawings based on incorrect guesses.

Real-time Feedback: Get immediate responses for each guess and see the updated word status.

**Requirements**

Python 3.x

**Installation**

Clone the repository:


git clone 
```
https://github.com/your-username/text-hangman.git
```

Navigate to the project directory:
```
cd 
text-hangman
```

Run the game:

```
python hangman.py
```

**How to Play**

Select Difficulty: Choose a difficulty level from easy, medium, or hard.

Guess the Word: Enter letters one at a time. You have 7 incorrect guesses allowed.

Win or Lose: The game ends when you either guess the word correctly or exhaust all guesses.

**code overview**

words: Dictionary with word lists for each difficulty level.

hangman: List of strings depicting hangman figures.

select_word(difficulty): Function to select a random word based on the chosen difficulty.

display_hangman(incorrect_guesses): Function to display the hangman figure corresponding to the number of incorrect guesses.

play_hangman(): Main function that handles game logic, including user input and guessing mechanics.

main(): Entry point to start the game and manage replay options.

**Contributing**

Contributions are welcome! Fork the repository, make changes, and submit pull requests to enhance the game or fix issues.
