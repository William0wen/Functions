def longest_word(word_list):
    longest = ""
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    return longest


# Main

words = []
word_ = ""

while word_ != "1":
    word_ = input("Enter word to list (or [1] to end): ")
    words.append(word_)

print(f"The longest word in {words} is {longest_word(words)}.")

