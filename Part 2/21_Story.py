words = ""
last_word = ""

while True:
    word = input("Please type in a word: ")
    
    if word == "end" or word == last_word:
        print(words)
        break
    words += word + " "
    last_word = word