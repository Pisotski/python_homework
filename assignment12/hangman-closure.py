def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())
        # iterate through each character in the secret word.
        # append character if it's in guesses list, otherwise _
        display = "".join(
            [char if char.lower() in guesses else "_" for char in secret_word]
        )
        print(f"Current word: {display}")
        # all function will return True if everything in this iteration is True
        # loop through the secret_word, check if that character is in guesses array
        return all(char.lower() in guesses for char in secret_word)

    return hangman_closure


if __name__ == "__main__":
    secret = input("Enter the secret word: ")
    hangman = make_hangman(secret)

    print("\nStart guessing characters!\n")

    while True:
        guess = input("Guess a character: ")
        if not guess or len(guess) != 1:
            print("Please enter a single character.")
            continue

        if hangman(guess):
            print(f"\nCongratulations! The word was: {secret}")
            break
