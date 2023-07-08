import random
import time
import requests

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by seewah\n")
name = input("Enter your name: ")



print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)


# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global full_word
    global already_guessed
    global length
    global play_game
    global game_difficulty
    valid_game_difficulty_choice = False


    while not valid_game_difficulty_choice:

        game_difficulty = input("enter 1 for easy, 2 for medium, 3 for hard: ")

        if game_difficulty == "1":
            mode = "easy"
            valid_game_difficulty_choice = True
        elif game_difficulty == "2":
            mode = "medium"
            valid_game_difficulty_choice = True
        elif game_difficulty == "3":
            mode = "hard"
            valid_game_difficulty_choice = True
        else:
            valid_game_difficulty_choice = False

    print(f'You have selected {mode} mode')



    while True:
        word = fetch_word()
        if game_difficulty == '1':
            if len(word) < 5:
                break
            else:
                continue
        elif game_difficulty == '2':
            if len(word) < 8:
                break
            else:
                continue
        else:
            if len(word) <= 8:
                continue
            else:
                break

    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    # print(word)


# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()


# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word)  # Display the actual word
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


def fetch_word():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    if response.status_code == 200:
        word_to_guess = response.json()
        word = word_to_guess[0]
    else:
        print("Failed to retrieve words from the API. Using a default wordlist.")
        with open("wordlist.txt", 'r') as fh:
            word_to_guess = [line.strip() for line in fh]
        word = random.choice(word_to_guess)
    return word


main()

hangman()
