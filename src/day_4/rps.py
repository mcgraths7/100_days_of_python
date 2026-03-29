import random

rock = """
     _______
---'    ____)
       (_____)
       (_____)
       (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
        _______)
        _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
      __________)
      (____)
---.__(___)

"""


def get_input(prompt, choices):
    while True:
        choice = input(prompt)
        if choice.lower() not in choices:
            print("You made an invalid choice. Please try again.")
            continue
        return choice


def print_choice(choice):
    if choice == "r":
        print(rock)
    elif choice == "p":
        print(paper)
    elif choice == "s":
        print(scissors)


def rps():
    choice = get_input("(r)ock, (p)aper, or (s)cissor?\n>>> ", ["r", "p", "s"])
    opponent = random.choice(["r", "p", "s"])

    print("You threw:")
    print_choice(choice)
    print("Your opponent threw:")
    print_choice(opponent)

    if (
        (choice == "r" and opponent == "r")
        or (choice == "p" and opponent == "p")
        or (choice == "s" and opponent == "s")
    ):
        print("It's a draw!")
    if (
        (choice == "r" and opponent == "s")
        or (choice == "p" and opponent == "r")
        or (choice == "s" and opponent == "p")
    ):
        print("You win!")
    if (
        (choice == "r" and opponent == "p")
        or (choice == "p" and opponent == "s")
        or (choice == "s" and opponent == "r")
    ):
        print("You lose!")
