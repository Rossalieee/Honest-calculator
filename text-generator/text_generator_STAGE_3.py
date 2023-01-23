from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter

file_name = input("Enter file name: ")
f = open(f"{file_name}", "r", encoding="utf-8")

text = f.read()
f.close()
tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(text)

bigram_list = list(bigrams(tokens))

freq_counter = Counter(bigram_list)

new_dict = {}
for item in freq_counter.items():
    key = item[0][0]
    value = item[0][1]
    count = item[1]
    new_dict.setdefault(key, {})
    new_dict[key][value] = count

while True:
    user_input = input("Enter a word:")
    if user_input == "exit":
        break
    else:
        try:
            tails_dict = new_dict[user_input]
            tails_dict = dict(sorted(tails_dict.items(), key=lambda item: item[1], reverse=True))
            print(f"Head: {user_input}")
            for item in tails_dict.items():
                print(f"Tail: {item[0]} Count: {item[1]}")
        except KeyError:
            print("Key Error. The requested word is not in the model. Please input another word.")
