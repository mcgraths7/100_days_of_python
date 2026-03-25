def get_input(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice.lower() not in valid_choices:
            print("You made an invalid choice. Please try again.")
            continue
        return choice.lower()


def pirate_adventure():
    print("""
        |    |    |
       )_)  )_)  )_)
      )___))___))___)\
     )____)____)_____)\\
   _____|____|____|____\\\__
---------\                   /---------
^^^^^ ^^^^^^^^^^^^^^^^^^^^^
^^^^      ^^^^     ^^^    ^^
   ^^^^      ^^^

      ~  ~  ~  ~  ~


██████╗ ██╗██████╗  █████╗ ████████╗███████╗
██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██████╔╝██║██████╔╝███████║   ██║   █████╗
██╔═══╝ ██║██╔══██╗██╔══██║   ██║   ██╔══╝
██║     ██║██║  ██║██║  ██║   ██║   ███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

█████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
        """)

    print("\nYou are captain of a scrappy pirate crew sailing the Grey Tide.")
    print("Rumor speaks of treasure hidden somewhere in these waters.\n")

    # 1
    choice1 = get_input(
        "A storm splits your path. Do you sail into the (storm) or skirt around it (coast)? ",
        ["storm", "coast"],
    )

    if choice1 == "storm":
        # 2A
        choice2 = get_input(
            "Through the storm you spot something massive. Investigate the (wreck) or chase a glowing (light)? ",
            ["wreck", "light"],
        )

        if choice2 == "wreck":
            # ENDING 1 — Abandoned Ship
            print("\nYou board a massive, legendary pirate ship—long abandoned.")
            print("Your crew stares in awe. With some work, she could sail again.")
            print("You order repairs to begin. A new legend is about to be born.\n")
            return

        else:  # light
            # 3A
            choice3 = get_input(
                "The light leads to a cave. Enter the (cave) or keep sailing (forward)? ",
                ["cave", "forward"],
            )

            if choice3 == "cave":
                # 4A
                choice4 = get_input(
                    "Inside: a chest and a sleeping parrot. Open the (chest) or grab the (parrot)? ",
                    ["chest", "parrot"],
                )

                if choice4 == "chest":
                    # GOLDEN PATH — Treasure
                    print("\nGold. Mountains of it.")
                    print("You’ve found the treasure of the Grey Tide.")
                    print("Your crew erupts. You are now absurdly rich.\n")
                    return
                else:
                    # COMICAL END
                    print(
                        "\nThe parrot wakes up furious and calls in about 200 friends."
                    )
                    print("You retreat, covered in feathers and shame.")
                    print("No treasure. Just bird-related regret.\n")
                    return

            else:
                # COMICAL END
                print("\nYou sail forward straight into a fog bank.")
                print("Hours later, you realize you’ve been circling the same rock.")
                print("The crew quietly loses confidence in you.\n")
                return

    else:  # coast
        # 2B
        choice2 = get_input(
            "Along the coast you see a port and a jungle. Dock at the (port) or explore the (jungle)? ",
            ["port", "jungle"],
        )

        if choice2 == "port":
            # ENDING 2 — Pirate Haven
            print("\nYou’ve found a hidden pirate haven.")
            print("Ships from every corner of the sea fill the harbor.")
            print("You and your crew spend the night drinking with other pirates.")
            print("No treasure—but a damn good time.\n")
            return

        else:  # jungle
            # 3B
            choice3 = get_input(
                "In the jungle: follow a (map) you found or chase a suspicious (monkey)? ",
                ["map", "monkey"],
            )

            if choice3 == "map":
                # 4B
                choice4 = get_input(
                    "The map leads to ruins. Enter the (ruins) or dig at an (x) marked spot? ",
                    ["ruins", "x"],
                )

                if choice4 == "x":
                    # GOLDEN PATH — Treasure
                    print("\nYou strike wood. Then gold.")
                    print("You’ve uncovered a buried treasure chest.")
                    print("Your crew cheers—you did it.\n")
                    return
                else:
                    # COMICAL END
                    print("\nThe ruins collapse immediately upon entry.")
                    print("You escape, but your dignity does not.\n")
                    return

            else:
                # COMICAL END
                print("\nThe monkey leads you in circles for hours.")
                print("It steals your hat. You never see it again.\n")
                return
