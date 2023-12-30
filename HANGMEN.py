import random

def choose_word():
    words = ["python", "hangman", "programming", "gaming", "challenge", "developer", "learning"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman_game():
    print("Welcome to Hangman!")
    
    # Choose a random word
    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 6  # Adjust the number of attempts as needed

    while attempts_left > 0:
        # Display the current state of the word
        current_display = display_word(secret_word, guessed_letters)
        print(f"Word: {current_display}")
        
        # Ask the player for a letter guess
        guess = input("Enter a letter: ").lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess not in secret_word:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")
        else:
            print("Correct guess!")

        # Check if the player has won
        if set(guessed_letters) >= set(secret_word):
            print(f"Congratulations! You guessed the word '{secret_word}'!")
            break

    else:
        print(f"Sorry, you've run out of attempts. The correct word was '{secret_word}'.")

if __name__ == "__main__":
    hangman_game()
