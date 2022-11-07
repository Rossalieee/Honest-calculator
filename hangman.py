import random

words_list = ["python", "java", "swift", "javascript"]
wins = 0
fails = 0


def input_check(x):
    if len(x) != 1:
        print("Please, input a single letter.")
    elif not x.islower():
        print("Please, enter a lowercase letter from the English alphabet.")
    else:
        print("You've already guessed this letter.")


def play():
    global wins
    global fails
    chosen_word = random.choice(words_list)
    chosen_word_list = list(chosen_word)
    hidden_word = list("-" * len(chosen_word))
    counter = 0
    attempts_total = 8
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    while True:
        if hidden_word != chosen_word_list:
            if counter < attempts_total:
                print("\n" + "".join(hidden_word))
                user_answer = input("Input a letter:")
                if user_answer not in alphabet:
                    input_check(user_answer)
                elif user_answer in chosen_word:
                    for index, letter in enumerate(chosen_word):
                        if letter == user_answer:
                            hidden_word[index] = user_answer
                    alphabet.discard(user_answer)
                else:
                    print("That letter doesn't appear in the word.")
                    counter += 1
                    alphabet.discard(user_answer)
            else:
                print("\nYou lost!")
                fails += 1
                break
        else:
            print("\n" + "".join(hidden_word))
            print(f"You guessed the word {chosen_word}!\nYou survived!")
            wins += 1
            break


def results():
    print(f"You won: {wins} times")
    print(f"You lost: {fails} times")


def hangman():
    print("H A N G M A N")
    while True:
        main_menu = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
        if main_menu == "play":
            play()
        elif main_menu == "results":
            results()
        else:
            break


hangman()