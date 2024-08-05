from collections import Counter
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def get_trigram_frequencies(text):
    processed_text = preprocess_text(text)
    words = processed_text.split()
    trigrams = zip(words, words[1:], words[2:])
    trigram_frequencies = Counter(trigrams)
    return trigram_frequencies

text = """
Natural Language Processing (NLP) is a sub-field of artificial intelligence (AI) 
that focuses on the interaction between computers and humans through natural language. 
The ultimate objective of NLP is to read, decipher, understand, and make sense of human languages 
in a manner that is valuable.
"""

trigram_frequencies = get_trigram_frequencies(text)

print("Trigram Frequencies:")
for trigram, freq in trigram_frequencies.items():
    print(f"{trigram}: {freq}")
