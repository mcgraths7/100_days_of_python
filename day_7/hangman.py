import random

# Choose random word
#
#
with open("formatted.txt") as f:
    possible_words = [line.strip() for line in f if line.strip()]


def generate_starting_state():
    chosen_word = random.choice(possible_words)
    current_lives = 6

    revealed_chars = []
    guessed_chars = set()
    for _ in chosen_word:
        revealed_chars.append("_")
    return current_lives, chosen_word, revealed_chars, guessed_chars


def make_guess(current_lives, chosen_word, revealed_chars, guessed_chars):
    print(f"============{current_lives}/6 lives remaining============")
    print(f"Already guessed: {guessed_chars}")
    print(f"Current progress: {revealed_chars}")
    print("==========================================================")
    guessed_char = input("Please pick a letter\n>>> ")

    if guessed_char in guessed_chars:
        print("You already guessed that letter. Try again.")
    elif guessed_char in chosen_word:
        for i in range(0, len(revealed_chars)):
            if guessed_char == chosen_word[i]:
                revealed_chars[i] = guessed_char
    else:
        current_lives -= 1
    guessed_chars.add(guessed_char)
    return current_lives, revealed_chars, guessed_chars


def hangman():
    current_lives, chosen_word, revealed_chars, guessed_chars = (
        generate_starting_state()
    )

    while current_lives > 0 and chosen_word != "".join(revealed_chars):
        current_lives, revealed_chars, guessed_chars = make_guess(
            current_lives, chosen_word, revealed_chars, guessed_chars
        )

        if current_lives == 0:
            print("You lose!")
            print(f"The word was {chosen_word}")
            return
        elif chosen_word == "".join(guessed_chars):
            print("You win!")
            print(f"The word was {chosen_word}")
            return
        else:
            continue
