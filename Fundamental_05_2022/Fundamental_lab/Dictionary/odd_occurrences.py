'''
words_dict = {}

for word in input().split(' '):
    if word.lower() not in words_dict:
        words_dict[word.lower()] = 0
    words_dict[word.lower()] += 1

for a,b in words_dict.items():
    if b % 2 != 0:
      print(a,end=' ')

 '''

from collections import defaultdict

words = input().split(' ')
counter_of_words = defaultdict(int)
print (counter_of_words)
for word in words:
    counter_of_words[word.lower()] += 1

print (counter_of_words)
 

print(' '.join([word for word, count in counter_of_words.items() if count % 2 != 0]))
