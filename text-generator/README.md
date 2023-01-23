# [Text Generator Project](https://hyperskill.org/projects/134)
Program predicting the next word in a pseudo-sentence based on the previous words in sequence. Created while doing python course on hyperskill.org. General schema and guidelines were provided by the website but solution was designed on my own. It was the opportunity to get better understanding of **natural language processing**, preprocessing and NLTK python library.

**Libraries/tools used:**
* NLTK (bigrams, WhiteSpaceTokenize,
* collections.Counter
* random


## Project Stages:

### Stage 1
**About:** In Natural Language Processing (NLP), most work starts by obtaining and preprocessing a text corpus. Corpus is a collection of textual data. In this case our corpus contains the entire script of *Game of Thrones*. For most linguistic tasks, the corpus has to be processed before we can access all the important information. One of the most basic operations is **tokenization**. In NLP, an individual text element (in most cases, a single word) is called a token, and the process of breaking the corpus into tokens is called tokenization.

As the corpus will be used to "train" a probabilistic model that will predict the next word in a chain of words, the generated text will resemble the style and vocabulary of the source material. The naturalness of the generated text depends on the data. The bigger the corpus, the better the results.

**Objectives:**
* Open and read the corpus from the provided file `corpus.txt`. The filename should be specified as user input.
* Break the corpus into individual words. Use the simplest form of tokenization: tokens are separated by whitespace characters such as spaces, tabulation, and newline characters. Punctuation marks should be left untouched since later on, they will play an important role in signaling where a sentence should end.
* Acquire and print the following information about the corpus under the section of the output called `Corpus statistics`:
  * the number of all tokens;
  * the number of all unique tokens, that is, the number of tokens without repetition.
* Take an integer as user input and print the token with the corresponding index. Repeat this process until the string `exit` is input. Also, make sure that the input index is actually an integer that falls in the range of the corpus. If that is not the case, print an error message and request a new input.


### Stage 2
**About:** To study how texts are structured, we usually have to take into consideration not just individual words but sequences of words and the relationships between them. These sequences might consist of any number of words, but usually, the number is limited to only two or three. A sequence of any number of adjacent tokens is called an n-gram, where n is the number of tokens. A sequence of two adjacent tokens is called a **bigram**. 

When referring to bigrams in this project, we divide them into two parts: **head** and **tail**. In our case, the first token of the bigram is the head and the second token is the tail. For example, in the bigram `good night`, `good` is the head and `night` is the tail.

**Objectives:**
* Transform the corpus into a collection of bigrams. The results should contain all the possible bigrams from the corpus, which means that:
 * Every token from the corpus should be a head of a bigram with the exception of the last token which cannot become a head since nothing follows it;
 * Every token from the corpus should be a tail of a bigram with the exception of the first token which cannot possibly be the tail of a bigram because nothing precedes it.
* Output the number of all bigrams in the corpus.
* Take an integer as user input and print the bigrams with the corresponding index. Repeat this process until the string `exit` is input. Also, make sure that the input is actually an integer that falls in the range of the collection of bigrams. If that is not the case, print an error message and request a new input. 
* Each bigram should have the format `Head: [head] Tail: [tail]` and should be printed in a new line.

### Stage 3
**About:** 


**Objectives:**


### Stage 4
**About:** 


**Objectives:**


### Stage 5
**About:** 


**Objectives:**

