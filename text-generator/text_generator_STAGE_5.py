from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from collections import Counter
import random

file_name = input()
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

sentence_endings = [".", "?", "!"]


def generate_first_word():
    while True:
        first_word = random.choice(tokens)
        if first_word[0].isupper() is False:
            continue
        if first_word[-1] in sentence_endings:
            continue
        break
    return first_word


def generate_next_word(prev_word):
    tails_dict = new_dict[prev_word]
    tails_dict = dict(sorted(tails_dict.items(), key=lambda item: item[1], reverse=True))
    next_word = random.choices(list(tails_dict.keys()), weights=list(tails_dict.values()))
    next_word = "".join(next_word)
    return next_word


def generate_sentence():
    previous_word = generate_first_word()
    sentence = [previous_word]
    while True:
        if len(sentence) < 5:
            next_word = generate_next_word(previous_word)
            sentence.append(next_word)
            previous_word = next_word
        elif sentence[-1][-1] not in sentence_endings:
            next_word = generate_next_word(previous_word)
            sentence.append(next_word)
            previous_word = next_word
        else:
            break
    return sentence


for i in range(0, 10):
    print(" ".join(generate_sentence()))
