from collections import Counter
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def get_unigram_frequencies(text):
    processed_text = preprocess_text(text)
    words = processed_text.split()
    unigram_frequencies = Counter(words)
    return unigram_frequencies

text = """
Natural Language Processing (NLP) is a sub-field of artificial intelligence (AI) 
that focuses on the interaction between computers and humans through natural language. 
The ultimate objective of NLP is to read, decipher, understand, and make sense of human languages 
in a manner that is valuable.
"""

unigram_frequencies = get_unigram_frequencies(text)

print("Unigram Frequencies:")
for word, freq in unigram_frequencies.items():
    print(f"'{word}': {freq}")
