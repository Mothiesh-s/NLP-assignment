from collections import Counter, defaultdict
import re

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

text = """
Natural Language Processing (NLP) is a sub-field of artificial intelligence (AI) 
that focuses on the interaction between computers and humans through natural language. 
The ultimate objective of NLP is to read, decipher, understand, and make sense of human languages 
in a manner that is valuable.
"""

bigram_probabilities = get_bigram_probabilities(text)

print("Bigram Probabilities:")
for w1, following_words in bigram_probabilities.items():
    for w2, prob in following_words.items():
        print(f"P({w2} | {w1}) = {prob:.4f}")
