def get_input(
    prompt,
    cast=str,
    choices=None,
    error_msg="Invalid input. Try again.",
):
    while True:
        raw = input(prompt)

        # Normalize emptiness
        if raw is None:
            raw = ""
        raw_stripped = raw.strip()

        if raw_stripped == "":
            print("Input cannot be empty.")
            continue

        # Cast
        try:
            value = raw_stripped if cast is str else cast(raw_stripped)
        except (ValueError, TypeError):
            print(error_msg)
            continue

        # Choices check
        if choices is not None and value not in choices:
            print(f"Choose one of: {choices}")
            continue

        return value
