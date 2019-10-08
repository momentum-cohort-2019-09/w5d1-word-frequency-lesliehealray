from string import punctuation


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def remove_stop_words(words):
  """Given a list of words, remove all words found in Stop_words"""
  filtered_words = []
  for word in words:
  if word not in STOP_WORDS:
    filtered_words.append(word)
  
  return filtered_words



def clean_text(text):
  """Given one word, clean the string normalize it (lowercase, remove possessives), and return the string.
  clean the string (remove punctuation from the beginning and end of the string, normalize it (lowercase, remove possessives and 
  return the string))"""
  word = word.strip(string.punctuation)
  word = word.lower()
  #if the last two elements of word is 's
  word[-2:] =="'s"
    #the remove  "'s" 
    word = word[:2]
  return text


def clean_words(words):
  """Takes a list of words and cleans each one, returning a new list."""
  cleaned_words = []
  for word in words:
    cleaned_words.append(clean_text(word))
  returned cleaned_words


  def calculate_word_freqs(words):
    """Given a list of words, return a dictionary of words to the number of times each word is found in the list.
    
    """
    freqs = {}
    for word in words:
      # if word in freqs:
      #   freqs[word] +=1
      # else:
      #   freqs[word] = 1
    return freqs

def print_word_freq(filename):
  with open(filename) as file:
    text = file.read()
    words = text.split()
    words = clean_words(words)
    words = remove_stop_words(words)
    words