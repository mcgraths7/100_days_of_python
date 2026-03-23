def loop_input(cast_func, error_msg="Invalid input", validator=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                raw = func(*args, **kwargs)

                if not raw.strip():
                    print("Input cannot be empty")
                    continue

                try:
                    value = cast_func(raw)

                    if validator and not validator(value):
                        print("Value not allowed")
                        continue

                    return value

                except ValueError:
                    print(error_msg)

        return wrapper

    return decorator


@loop_input(float, "Value must be a positive number", validator=lambda x: x > 0.0)
def get_input(prompt):
    return input(prompt)


def get_total_with_tip(total, tip_percent):
    return total + (tip_percent * total / 100)


def calculate_per_person(total_bill, tip_percent, num_guests):
    return get_total_with_tip(total_bill, tip_percent) / num_guests


def calc_tip():
    total_bill = get_input("What was the total bill?\n>> $")
    tip_percent = get_input("What % tip did you leave (e.g. 10, 15, 20)?\n>> ")
    total_guests = get_input("How many guests in your party?\n>> ")

    per_person = calculate_per_person(total_bill, tip_percent, total_guests)
    print(f"You must pay ${per_person:.2f}")
