from collections import defaultdict
tokens = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog",
    "cat"
]

freq = defaultdict(int)

for token in tokens:
    freq[token] += 1

print(freq) 