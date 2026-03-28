import random

# Letters (both lowercase and uppercase)
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# Numbers
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Common symbols accepted in most password fields
symbols = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
]

numbers_symbols = numbers + symbols

with open("formatted.txt") as f:
    lines = [line.strip() for line in f if line.strip()]


def get_input(prompt, min=1, choices=[]):
    while True:
        choice = input(prompt)
        if choice.strip() == "" and (choice in choices if len(choices) > 0 else True):
            print("You made an invalid choice. Please try again.")
            continue
        elif len(choice) < min:
            print(
                "Password is too short, please enter a higher number (minimum 12 characters)."
            )
            continue
        return choice


def generate_random():
    pw_length = int(
        get_input("How long should your password be (minimum 12 characters?\n>>> ")
    )

    num_numbers = int(get_input("How many numbers?\n>>> "))
    num_symbols = int(get_input("How many symbols?\n>>> "))
    num_letters = pw_length - num_numbers - num_symbols
    pw_chars = []

    if num_letters > 0:
        for i in range(0, num_letters):
            pw_chars.append(random.choice(letters))
    if num_symbols > 0:
        for i in range(0, num_symbols):
            pw_chars.append(random.choice(symbols))
    if num_numbers > 0:
        for i in range(0, num_numbers):
            pw_chars.append(random.choice(numbers))

    random.shuffle(pw_chars)

    return "".join(pw_chars)


def generate_memorable():
    num_words = int(
        get_input("How many words should your password include? (minimum 3?\n>>> ")
    )

    separator_choice = get_input(
        "Separated by (n)umbers, (s)ymbols, or (b)oth??\n>>> ",
        choices=["n", "s", "b"],
    )

    pw_parts = []

    for i in range(0, num_words):
        random_word = random.choice(lines)
        separator = random.choice(
            {"n": numbers, "s": symbols, "b": numbers_symbols}[separator_choice]
        )
        pw_parts.append(random_word + separator)
    return "".join(pw_parts)


def generate():
    mode = get_input("(r)andom or (m)emorable password?\n>>> ", choices=["r", "m"])
    password = ""
    if mode == "r":
        password = generate_random()
    elif mode == "m":
        password = generate_memorable()
    else:
        print("invalid")
    return password
