import string
import re

frequency={}

with open('seneca_falls.txt', 'r') as document_text:
  t_string = document_text.read().lower()
  match_pattern = re.findall(r'\b[a-z]{3,15}\b', t_string)
 
for word in match_pattern:
  count = frequency.get(word, 0)
  frequency[word] = count + 1

  frequency_list = frequency.keys()

for words in frequency_list:
  print (words, frequency[words])

  
