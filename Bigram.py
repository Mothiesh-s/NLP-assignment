from collections import Counter
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def get_bigram_frequencies(text):
    processed_text = preprocess_text(text)
    words = processed_text.split()
    bigrams = zip(words, words[1:])
    bigram_frequencies = Counter(bigrams)
    return bigram_frequencies

text = """
Natural Language Processing (NLP) is a sub-field of artificial intelligence (AI) 
that focuses on the interaction between computers and humans through natural language. 
The ultimate objective of NLP is to read, decipher, understand, and make sense of human languages 
in a manner that is valuable.
"""

bigram_frequencies = get_bigram_frequencies(text)

print("Bigram Frequencies:")
for bigram, freq in bigram_frequencies.items():
    print(f"{bigram}: {freq}")
