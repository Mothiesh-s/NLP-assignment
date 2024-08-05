from collections import Counter, defaultdict
import re
import random

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def get_bigram_probabilities(text):
    processed_text = preprocess_text(text)
    words = processed_text.split()
    bigrams = zip(words, words[1:])
    bigram_counts = Counter(bigrams)
    unigram_counts = Counter(words)

    bigram_probabilities = defaultdict(dict)
    for (w1, w2), count in bigram_counts.items():
        bigram_probabilities[w1][w2] = count / unigram_counts[w1]

    return bigram_probabilities

def predict_next_word(current_word, bigram_probabilities):
    if current_word in bigram_probabilities:
        next_words = list(bigram_probabilities[current_word].keys())
        probabilities = list(bigram_probabilities[current_word].values())
        return random.choices(next_words, probabilities)[0]
    else:
        return None

text = """
Natural Language Processing (NLP) is a sub-field of artificial intelligence (AI) 
that focuses on the interaction between computers and humans through natural language. 
The ultimate objective of NLP is to read, decipher, understand, and make sense of human languages 
in a manner that is valuable.
"""

bigram_probabilities = get_bigram_probabilities(text)

current_word = "natural"
next_word = predict_next_word(current_word, bigram_probabilities)
print(f"Next word prediction for '{current_word}': {next_word}")
