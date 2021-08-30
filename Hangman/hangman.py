import random


def hangman():
    # word of list fruites
    word = random.choice(["apple", "banana", "orange", "coconut", "strawberry",
                         "lime", "grapefruit", "lemon", "kumquat", "blueberry", "melon"])
    validateChar = "abcdefghijklmnopqrstuvwxyz"
    turn = 10
    guessed = ""

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessed:
                main += letter
            else:
                main += "_"

        if main == word:
            print(main)
            print("You won")
            break

        print("Guess the word ", main)
        guess = input()

        if guess in validateChar:
            guessed = guessed + guess
        else:
            print("Invalid character")
            guess = input("Guess a letter: ")
        if guess not in word:
            turn = turn - 1
            print("Wrong")
            print("You have", turn, "more guesses")
            if turn == 0:
                print("You Lose")
                print("The word was", word)
                break


name = input("Enter your name: ")
print("Welcome", name, " to Game")
print("-----------------")
print("You have 10 tries to guess the word")
print("-----------------")
print(hangman())
