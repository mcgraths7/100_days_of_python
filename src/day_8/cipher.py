from src.utils.input_helpers import get_input


def shift_char(char, shift_value):
    return chr(
        (ord(char) - ord("a") + shift_value) % 26 + ord("a")
    )  # convert to unicode, wrap back to beginning


def encode(message, shift_value):
    encoded_message = ""
    for char in message:
        encoded_message += shift_char(char, shift_value)
    return encoded_message


def decode(encoded_message, shift_value):
    decoded_message = ""
    for char in encoded_message:
        decoded_message += shift_char(char, shift_value * -1)
    return decoded_message


def cipher():
    mode = get_input("Would you like to (e)ncode or (d)ecode?\n>>> ")
    message = get_input("What is the message? (all lowercase, no spaces)\n>>> ")
    shift_value = get_input("What is the shift value?\n>>> ", cast=int)

    mode_text = "encoded" if mode == "e" else "decoded"
    new_message = (
        encode(message, shift_value) if mode == "e" else decode(message, shift_value)
    )

    print(f"Your {mode_text} message is {new_message}")
