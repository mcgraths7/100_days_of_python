import random

from src.utils.input_helpers import get_input

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
    return {
        "deck": shuffle(deck),
        "player_hand": [],
        "dealer_hand": [],
    }


def reset_hands(state):
    return {"deck": state["deck"], "player_hand": [], "dealer_hand": []}


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
    }


def hit_dealer(state):
    new_deck, new_hand = deal(state["deck"], state["dealer_hand"])

    return {
        "deck": new_deck,
        "player_hand": state["player_hand"],
        "dealer_hand": new_hand,
    }


def hit(state, player):
    if len(state["deck"]) == 0:
        print("Deck exhausted. Shuffling new deck in.")
        state = {
            "deck": shuffle(starting_deck),
            "player_hand": state["player_hand"],
            "dealer_hand": state["dealer_hand"],
        }

    if player == "player":
        state = hit_player(state)
    elif player == "dealer":
        state = hit_dealer(state)

    return state


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
    ]  # List composition


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
        return True
    if dealer_bj and not player_bj:
        print("Dealer has blackjack. You lose!")
        return True
    if dealer_bj and player_bj:
        print("Both players have blackjack! It's a draw.")

    return False


# # # # # # # # #
# # # Main # # #
# # # # # # # #


def game_loop(state):

    if check_blackjack(state):
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
