import random

from src.utils.input_helpers import get_input
from src.utils.output_helpers import print_message

initial_state = {
    "difficulty": None,
    "total_guesses": None,
    "guesses_left": None,
    "current_guess": None,
    "magic_number": None,
    "message": None,
}

# Setup


def setup_game(state):
    difficulty = get_input(
        "Would you like to play on (easy) or (hard)?\n>>> ", choices=["easy", "hard"]
    )

    state["difficulty"] = difficulty

    state["total_guesses"] = 10 if difficulty == "easy" else 5

    state["guesses_left"] = state["total_guesses"]

    return state


# Actions


def guess(state):
    state["guesses_left"] -= 1

    guess = state["current_guess"]
    target = state["magic_number"]

    if guess == target:
        state["message"] = "You guessed correctly!"
    elif state["guesses_left"] == 0:
        state["message"] = f"You LOSE! Number was {target}"
    else:
        state["message"] = (
            f"You guessed {'too high' if guess > target else 'too low'}. Try again"
        )


def game_loop(state):
    while state["guesses_left"] > 0:
        state["current_guess"] = get_input(
            "Choose a number between 1 and 100\n>>> ", cast=int, choices=range(1, 100)
        )

        guess(state)
        print_message(state["message"])
        if state["current_guess"] == state["magic_number"]:
            break


def number_guesser():
    global initial_state
    game_state = {
        **initial_state,
        "magic_number": random.randint(1, 100),
    }
    game_state = setup_game(game_state)
    game_loop(game_state)
