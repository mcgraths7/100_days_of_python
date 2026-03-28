def has_double_chars(word):
    return any(a == b for a, b in zip(word, word[1:]))


with open("words.txt", "r") as infile, open("formatted.txt", "w") as outfile:
    for line in infile:
        word = line.strip()
        if 5 <= len(word) <= 10 and not has_double_chars(word):
            outfile.write(word + "\n")
