import os
import random

from src.utils.input_helpers import get_input

AUCTION_ITEMS = [
    "Gilded Toenail Clippings – A jar of perfectly preserved toenail clippings from a long-forgotten duke.",
    "Self-Turning Teacup – A porcelain teacup that refuses to stay still unless complimented.",
    "Invisible Paintbrush – A brush that paints only what nobody can see.",
    "Quantum Sock – A single sock that may or may not exist at any given time.",
    "Time-Traveling Toaster – Toasts bread yesterday, today, or tomorrow.",
    "Eternal Bubblegum – Chew once, and it never loses flavor.",
    "Miniature Cloud in a Jar – A fluffy cloud contained, with occasional lightning.",
    "Banana-Powered Clock – Tells time based on ripeness of the banana inside.",
    "Shapeshifting Spoon – Changes shape depending on what it thinks you want to eat.",
    "Haunted Lint Ball – Collects whispers from clothes long discarded.",
    "Portable Black Hole – Perfect for losing things permanently.",
    "Laughing Teapot – Bursts into giggles whenever it’s poured.",
    "Gravity-Defying Hat – Floats just above your head, never letting you forget it.",
    "Sock Puppet CEO – Runs a fake company, surprisingly competent.",
    "Upside-Down Mirror – Reflects the opposite of reality, mostly confusing.",
    "Whistling Doorknob – Sings random tunes when turned.",
    "Glow-in-the-Dark Mustache Wax – Ideal for nocturnal facial hair fashion.",
    "Miniature Tornado in a Teacup – Spirals wildly but harmlessly.",
    "Cursed Pencil – Writes whatever it wants, sometimes backwards.",
    "Soap That Never Lathers – A philosophical statement in bar form.",
    "Accordion That Only Plays Silence – The suspense is unbearable.",
    "Flying Carpet Tile – A single tile from a legendary flying carpet.",
    "Invisible Umbrella – Keeps you dry only in theory.",
    "Pet Rock with Wi-Fi – Rock has an online presence, updates daily.",
    "Jar of Forgotten Dreams – Smells faintly of ambition and regret.",
]


def high_bidder_second_bid(bidders_dict):
    if not bidders_dict:
        return None, None  # handle empty dict

    sorted_bidders = sorted(
        bidders_dict.items(), key=lambda item: item[1], reverse=True
    )

    high_bidder = sorted_bidders[0][0]
    second_bid = (
        sorted_bidders[0][1] if len(sorted_bidders) == 1 else sorted_bidders[1][1]
    )

    return high_bidder, second_bid


def auction():
    bidders = {}
    auction_item = random.choice(AUCTION_ITEMS)

    print("===================================================================")
    print("====================Welcome to the auction!========================")
    print("===================================================================")
    print(f"On the auction block today is this {auction_item}")

    while True:
        bidder_name = get_input("What is your name?\n>>> ")
        bidder_bid = get_input("What is your bid?\n >>> $", cast=float)
        additional_bidders = get_input(
            "Are there additional bidders? (y/n)\n>>> ", choices=["y", "n"]
        )

        bidders[bidder_name] = bidder_bid
        if additional_bidders == "y":
            # For Windows
            if os.name == "nt":
                os.system("cls")
            # For Linux or macOS
            else:
                os.system("clear")
            continue

        else:
            break

    high_bidder, second_highest_bid = high_bidder_second_bid(bidders)
    print(
        f"The winner of this auction is {high_bidder} with a bid of ${second_highest_bid:.2f}."
    )
