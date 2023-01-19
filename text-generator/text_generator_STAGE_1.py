from nltk.tokenize import WhitespaceTokenizer

file_name = input()
f = open(f"{file_name}", "r", encoding="utf-8")

text = f.read()
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(text)

all_tokens = len(tokens)
unique_tokens = len(set(tokens))

print(f"""Corpus statistics
All tokens: {all_tokens}
Unique tokens: {unique_tokens}""")

while True:
    user_input = input()
    if user_input == "exit":
        break
    else:
        try:
            token_index = int(user_input)
            print(tokens[token_index])
        except ValueError:
            print("Value Error. Please input an integer.")
        except TypeError:
            print("Type Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
