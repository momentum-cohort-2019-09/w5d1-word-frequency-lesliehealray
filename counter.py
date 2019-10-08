from string import punctuation
from collections import Counter

def print_word_freq(filename):
    with open(filename) as file_handler:
        words = file_handler.read().lower().split()
    punc = punctuation
    no_punc = [word.strip(punc) for word in words if word not in STOP_WORDS]
    Counter(no_punc.split()) 
    #introspects the kv pairs in the dictionary and returns them as a list of sorted (by value) tuples. 
    sorted_frequency = sorted(frequency.items(), key=lambda kv: kv[1], reverse = True)
    for word_count in sorted_frequency:
        # her | 33 *********************************
        print(f"{word_count[0]} | {word_count[1]} {'*' * word_count[1]}")
