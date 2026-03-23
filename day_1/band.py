def generate_band_name():
    while True:
        hometown = input("In what town did you grow up?\n>> ")
        if hometown != "":
            break
    while True:
        pet_name = input("What was the name of your first pet?\n>> ")
        if pet_name != "":
            break
    print(f"Your band name could be {hometown} {pet_name}.")
