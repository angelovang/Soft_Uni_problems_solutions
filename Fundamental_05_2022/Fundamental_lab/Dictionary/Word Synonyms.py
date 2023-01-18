from collections import defaultdict

synonyms = defaultdict(list)

n = int(input())

for i in range(n):
    word,syn = input() , input()
    synonyms[word].append(syn)

for word,syn in synonyms.items():
    print(f"{word} - {', '.join(syn)}")

