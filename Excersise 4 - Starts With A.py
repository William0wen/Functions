def starts_with_a(word_):
    if word_[0] == "A":
        return True
    else:
        return False


# Main
word = input("Enter the word: ").title()
print(starts_with_a(word))
