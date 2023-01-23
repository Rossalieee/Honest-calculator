from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter
import random

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

random_word = random.choice(tokens)
sentence = [random_word]
n = 1

for i in range(0, 10):
    for i in range(n, 10):
        tails_dict = new_dict[random_word]
        tails_dict = dict(sorted(tails_dict.items(), key=lambda item: item[1], reverse=True))
        tails_list = list(tails_dict.keys())
        weights_list = list(tails_dict.values())
        next_word = random.choices(tails_list, weights=weights_list)
        sentence += next_word
        random_word = "".join(next_word)
        n = 0
    print(" ".join(sentence))
    sentence = []
