# Hangman Game

This is a simple Hangman game implemented in Python.

## Description

The Hangman game allows players to guess a word by suggesting letters. Players have a limited number of incorrect guesses before the hangman is complete. The objective is to guess the word correctly before running out of guesses.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/hangman.git`
2. Navigate to the project directory: `cd hangman`
3. Install the required dependencies: `pip install requests`

## Usage

1. Run the game script: `python hangman.py`
2. Enter your name when prompted.
3. Follow the instructions on the screen to play the Hangman game.

## API Integration

The game retrieves words to guess from an external API that generates random words. If the API is unavailable, a default wordlist is used instead.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This Hangman game was developed by seewah.
- The random word API used in this project is provided by https://random-word-api.herokuapp.com/word.
