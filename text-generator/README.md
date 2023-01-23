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

**Example:**

![text_generator_stage_1](https://user-images.githubusercontent.com/107406800/214070893-0e332f4f-0a19-455f-915b-e3b145ca78c2.PNG)


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

**Example:**

![text_generator_stage_2](https://user-images.githubusercontent.com/107406800/214071034-5cf62158-5633-483e-87c0-598af69df349.PNG)


### Stage 3
**About:** A **Markov chain** is a statistical model in which the probability of each event depends on the previous event. It can be described as a set of states and transitions between them. Each transition has a probability that is determined by some kind of statistical data. In this project, a state corresponds to a token, and each transition represents going from one word of a sentence to another. The probability of transitions is calculated from the bigrams we collected in the previous stage. The basic idea of this project is that from a dictionary we can create a model that will consider all the possible transitions from one word to another and choose the most probable one based on the previous word.

This is the final step where we will work on creating a Markov chain model. We will use the data prepared in the first two stages and transform it into a model. This model will contain probabilistic information that will tell us what the next word in a chain might be.

**Objectives:**
* The data should be reorganized in such a way that every head is repeated only once, and all the possible tails can be directly accessed by querying that head.
* Instead of repeating tails every time they occur, each tail should appear only once and the number of repetitions should be stored as an integer. For example: head — `good`, tails — `night: 2`, `bye: 3`, `to: 2`, `boy: 1`.
* Take a string as user input and print all the possible tails and their corresponding counts. If the model does not contain the specified head print the following error message `Key Error. The requested word is not in the model. Please input another word.` and ask for another until it is valid. Repeat until the string `exit` is input.

**Example:**

![text_generator_stage_3](https://user-images.githubusercontent.com/107406800/214071120-2abdc75b-6d8b-49d3-8211-b1ffa1de8e18.PNG)


### Stage 4
**About:** The model can already be used to predict the next word in a chain by feeding it any head (of a bigram) from the corpus and retrieving the most probable tail from the corresponding entry. But how do we start the chain, what should be the first word?

Of course, we could choose a word manually, but this is an error-prone solution because we might take a word that is not in the corpus. A better way to start is to choose a random word from the corpus and feed it to the model so that it predicts the next word.
After the next word is acquired, it should be used to predict the following word, and so on, thus continuing the chain.

**Objectives:**
* Choose a random word from the corpus that will serve as the first word of the chain.
* The second word should be predicted by looking up the first word of the chain in the model and choosing the most probable next word from the set of possible follow-ups.
* The second step should be repeated until the length of the chain is 10 words, but this time, the current last word of the chain should be used to look up another probable word to continue the sentence.
* Using the algorithm described above, generate chains consisting of 10 tokens, join the resulting tokens together, and print them as a pseudo-sentence. Keep in mind that a pseudo-sentence can consist of multiple actual sentences, so having punctuation marks inside pseudo-sentences is completely valid.
* Generate and print 10 sentences like that. Keep in mind that every generated pseudo-sentence should be on a new line.

**Example:**

![text_generator_stage_4](https://user-images.githubusercontent.com/107406800/214071193-9ce661c7-ca67-48e6-8827-4114d5024ec3.PNG)


### Stage 5
**About:** As you can see, the algorithm is now capable of generating pseudo-random text based on Markov chains. The problem is that the resulting text does not resemble real sentences at all. First, the resulting text is always ten tokens long. Second, it does not always start with capital letters. Third, it usually does not even end with correct punctuation such as periods, exclamation marks, or question marks. We fix it in this stage.

**Objectives:**
* Make the algorithm more realistic by generating pseudo-sentences instead of just random text.
* The sentences that are being generated should:
 * always start with capitalized words ("This is beautiful.", "You are a great programmer!", etc.);
 * not start with a word that ends with a sentence-ending punctuation mark ("Okay.", "Nice.", "Good.", "Look!", "Jon!", etc.);
 * always end with a sentence-ending punctuation mark like `.`, `!`, or `?`;
 * should not be shorter than 5 tokens.
* Generate and print exactly 10 pseudo-sentences that meet these criteria. A pseudo-sentence should end when the first sentence-ending punctuation mark is encountered after the minimal sentence length (5 tokens) is reached.

**Example:**

![text_generator_stage_5](https://user-images.githubusercontent.com/107406800/214071243-22110b34-0a1a-40ab-a366-466cfbfec3c2.PNG)

