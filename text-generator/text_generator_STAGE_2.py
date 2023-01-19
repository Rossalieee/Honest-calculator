from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams

file_name = input()
f = open(f"{file_name}", "r", encoding="utf-8")

text = f.read()
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(text)

bigram_list = list(bigrams(tokens))

all_bigrams = len(bigram_list)

print(f"Number of bigrams: {all_bigrams}")

while True:
    user_input = input()
    if user_input == "exit":
        break
    else:
        try:
            bigram_index = int(user_input)
            print(f"Head: {bigram_list[bigram_index][0]} Tail: {bigram_list[bigram_index][1]}")
        except ValueError:
            print("Value Error. Please input an integer.")
        except TypeError:
            print("Type Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input a value that is not greater than the number of all bigrams.")
