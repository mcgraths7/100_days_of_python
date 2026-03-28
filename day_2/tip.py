def get_input(prompt):
    while True:
        choice = input(prompt)
        if choice.strip() == "":
            print("You made an invalid choice. Please try again.")
            continue
        return choice


def get_total_with_tip(total, tip_percent):
    return total + (tip_percent * total / 100)


def calculate_per_person(total_bill, tip_percent, num_guests):
    return get_total_with_tip(total_bill, tip_percent) / num_guests


def calc_tip():
    total_bill = float(get_input("What was the total bill?\n>> $"))
    tip_percent = float(get_input("What % tip did you leave (e.g. 10, 15, 20)?\n>> "))
    total_guests = int(get_input("How many guests in your party?\n>> "))

    per_person = calculate_per_person(total_bill, tip_percent, total_guests)
    print(f"You must pay ${per_person:.2f}")
