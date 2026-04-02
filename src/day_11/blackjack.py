import os
import random

from src.utils.input_helpers import get_input

file_name = "wagers.txt"
starting_balance = 1000

if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write(f"{starting_balance}\n")

starting_deck = [
    "2",
    "2",
    "2",
    "2",
    "3",
    "3",
    "3",
    "3",
    "4",
    "4",
    "4",
    "4",
    "5",
    "5",
    "5",
    "5",
    "6",
    "6",
    "6",
    "6",
    "7",
    "7",
    "7",
    "7",
    "8",
    "8",
    "8",
    "8",
    "9",
    "9",
    "9",
    "9",
    "10",
    "10",
    "10",
    "10",
    "J",
    "J",
    "J",
    "J",
    "Q",
    "Q",
    "Q",
    "Q",
    "K",
    "K",
    "K",
    "K",
    "A",
    "A",
    "A",
    "A",
]

value_map = {
    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

# # # # # # # # # #
# # # Helpers # # #
# # # # # # # # # #


def shuffle(deck):
    return random.sample(deck, len(deck))


def deal(deck, hand):
    card = deck[-1]
    new_deck = deck[:-1]
    new_hand = hand + [card]
    return new_deck, new_hand


def card_value(card):
    return value_map[card]


def sort_hand(hand):
    return sorted(hand, key=card_value)


def calculate_total(hand):
    total = 0

    for card in sort_hand(hand):
        if card == "A" and total >= 11:
            total += 1
        else:
            total += card_value(card)

    return total


def create_game_state(deck):
    with open(file_name, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines if line.strip()]

    balance = int(float(lines[-1]))
    print(f"Balance from last session: {balance}")
    return {
        "deck": shuffle(deck),
        "player_hand": [],
        "dealer_hand": [],
        "current_wager": 0,
        "balance": balance,
        "has_blackjack": False,
    }


def reset_hands(state):
    return {
        "deck": state["deck"],
        "player_hand": [],
        "dealer_hand": [],
        "current_wager": state["current_wager"],
        "balance": state["balance"],
        "has_blackjack": state["has_blackjack"],
    }


def get_wager(state):
    wager = get_input(
        f"How much would you like to bet? (Available balance: {state['balance']})\n>>> $",
        cast=int,
        choices=range(1, state["balance"]),
    )

    return {
        "deck": state["deck"],
        "player_hand": state["player_hand"],
        "dealer_hand": state["dealer_hand"],
        "current_wager": wager,
        "balance": state["balance"] - wager,
        "has_blackjack": state["has_blackjack"],
    }


def write_balance(state):
    with open(file_name, "w") as f:
        f.write(f"{state['balance']}\n")


def continue_playing():
    choice = get_input("Would you like to play again? (y/n)\n>>> ", choices=["y", "n"])

    return choice


# # # # # # # # # #
# # # Actions # # #
# # # # # # # # # #


def hit_player(state):
    new_deck, new_hand = deal(state["deck"], state["player_hand"])

    return {
        "deck": new_deck,
        "player_hand": new_hand,
        "dealer_hand": state["dealer_hand"],
        "current_wager": state["current_wager"],
        "balance": state["balance"],
        "has_blackjack": state["has_blackjack"],
    }


def hit_dealer(state):
    new_deck, new_hand = deal(state["deck"], state["dealer_hand"])

    return {
        "deck": new_deck,
        "player_hand": state["player_hand"],
        "dealer_hand": new_hand,
        "current_wager": state["current_wager"],
        "balance": state["balance"],
        "has_blackjack": state["has_blackjack"],
    }


def hit(state, player):
    if len(state["deck"]) == 0:
        print("Deck exhausted. Shuffling new deck in.")
        state = {
            "deck": shuffle(starting_deck),
            "player_hand": state["player_hand"],
            "dealer_hand": state["dealer_hand"],
            "current_wager": state["current_wager"],
            "balance": state["balance"],
            "has_blackjack": state["has_blackjack"],
        }

    if player == "player":
        state = hit_player(state)
    elif player == "dealer":
        state = hit_dealer(state)

    return state


def wager(state, amount):
    return {
        "deck": state["deck"],
        "player_hand": state["player_hand"],
        "dealer_hand": state["dealer_hand"],
        "current_wager": amount,
        "balance": state["balance"] - amount,
        "has_blackjack": state["has_blackjack"],
    }


def add_winnings(state, winner, has_blackjack):
    if winner == "player":
        winnings = state["current_wager"] * 1.5
        print(f"You won ${winnings:.2f}")
    elif winner == "dealer":
        winnings = 0
        print("You lost your wager")
    else:
        winnings = state["current_wager"]
        print("You get your wager back")

    return {
        "deck": state["deck"],
        "player_hand": state["player_hand"],
        "dealer_hand": state["dealer_hand"],
        "current_wager": int(state["current_wager"]),
        "balance": state["balance"] + winnings,
        "has_blackjack": has_blackjack,
    }


def player_turn(state):
    while True:
        total = calculate_total(state["player_hand"])
        print(f"\nYour hand: {format_hand(state['player_hand'])} (total: {total})")

        if total > 21:
            print("Bust! You lose!")
            return state, "player_bust"

        choice = get_input("Hit or stay? (h/s)\n>>> ", choices=["h", "s"])

        if choice == "h":
            state = hit(state, "player")
        else:
            return state, "player_stay"


def dealer_turn(state):
    print("\nDealer reveals hand:")

    while True:
        total = calculate_total(state["dealer_hand"])
        print(f"{format_hand(state['dealer_hand'], False, False)}")
        print(f"Dealer total: {total}")

        if total > 21:
            print("Dealer busts! You win!")
            return state, "dealer_bust"

        if total >= 17:
            print("Dealer stays.")
            return state, "dealer_stay"

        print("The dealer hits.")
        state = hit(state, "dealer")


def determine_winner(state):
    player_total = calculate_total(state["player_hand"])
    dealer_total = calculate_total(state["dealer_hand"])

    print(f"\nFinal totals — You: {player_total}, Dealer: {dealer_total}")

    if dealer_total > 21:
        return "player"
    if player_total > 21:
        return "dealer"
    if player_total > dealer_total:
        return "player"
    if dealer_total > player_total:
        return "dealer"
    return "push"


def initial_deal(state):
    state = hit(state, "player")
    state = hit(state, "dealer")
    state = hit(state, "player")
    state = hit(state, "dealer")

    return state


# # # # # # # # # # # # #
# # # Presentation # # #
# # # # # # # # # # # #


def format_hand(hand, is_dealer=False, initial_deal=True):
    return [
        "?" if idx == 0 and is_dealer and initial_deal else card
        for idx, card in enumerate(hand)
    ]


def print_hand(hand, is_dealer=False, initial_deal=True):
    label = "The dealers" if is_dealer else "Your"
    print(f"{label} hand is {format_hand(hand, is_dealer, initial_deal)}")


def has_blackjack(hand):
    return calculate_total(hand) == 21


def check_blackjack(state):
    print_hand(state["player_hand"])
    print_hand(state["dealer_hand"], True)

    player_bj = has_blackjack(state["player_hand"])
    dealer_bj = has_blackjack(state["dealer_hand"])

    if player_bj and not dealer_bj:
        print("Blackjack! You win!")
        state = add_winnings(state, "player", True)
        write_balance(state)
    if dealer_bj and not player_bj:
        print("Dealer has blackjack. You lose!")
        state = add_winnings(state, "dealer", True)
        write_balance(state)
    if dealer_bj and player_bj:
        print("Both players have blackjack! It's a draw.")
        state = add_winnings(state, None, True)
        write_balance(state)

    return state


# # # # # # # # #
# # # Main # # #
# # # # # # # #


def game_loop(state):

    state = get_wager(state)

    state = check_blackjack(state)

    if state["has_blackjack"]:
        return state

    state, result = player_turn(state)
    if result == "player_bust":
        return state

    state, result = dealer_turn(state)
    if result == "dealer_bust":
        return state

    winner = determine_winner(state)

    if winner == "player":
        print("You win!")

    elif winner == "dealer":
        print("You lose!")
    else:
        print("Push (tie).")

    state = add_winnings(state, winner, False)
    write_balance(state)

    return state


def blackjack():
    game_active = True
    state = create_game_state(starting_deck)
    state = initial_deal(state)

    while game_active:
        state = game_loop(state)
        if continue_playing() == "y":
            state = reset_hands(state)
            state = initial_deal(state)
        else:
            game_active = False
