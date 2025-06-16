
# using if condition to count
def countWords(word1):
    hashmap = {}

    for word in word1:
        if word in hashmap:
            hashmap[word] += 1
        else:
            hashmap[word] = 1

    return hashmap

# using dict.get()
def countWords1(word1):
    hashmap = {}
    for word in word1:
        hashmap[word] = hashmap.get(word, 0) + 1
    return hashmap

# uisng in-built function
from collections import defaultdict

def countWords2(words1):
    hashmap = defaultdict(int)
    for word in words1:
        hashmap[word] += 1
    return hashmap

word1 = ["kaify", "farzan", "kaify", "farzan"]
print(countWords(word1))
print(countWords1(word1))
print(countWords2(word1))