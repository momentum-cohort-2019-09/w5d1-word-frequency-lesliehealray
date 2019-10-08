from string import punctuation

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]



def print_word_freq(filename):
    with open(filename) as file_handler:
        words = file_handler.read().lower().split()
    punc = punctuation
    no_punc = [word.strip(punc) for word in words if word not in STOP_WORDS]
    frequency = {}
    for word in no_punc:
        #similar to .get() but will set key value pair for the missing key because it is not in the dictionary yet. .get() will not set the kv pair.
        frequency.setdefault(word, 0)
        frequency[word] += 1
    #introspects the kv pairs in the dictionary and returns them as a list of sorted (by value) tuples. 
    sorted_frequency = sorted(frequency.items(), key=lambda kv: kv[1], reverse = True)
    for word_count in sorted_frequency:
        # her | 33 *********************************
        print(f"{word_count[0]} | {word_count[1]} {'*' * word_count[1]}")

    

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
