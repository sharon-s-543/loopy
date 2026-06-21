from brute import add_word

with open("words.txt") as f:
    for line in f:
        add_word(line.strip())

print("Done.")
