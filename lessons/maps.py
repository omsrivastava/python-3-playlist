from random import shuffle

def jumble(word):
  anagram = list(word)
  shuffle(anagram)
  return ''.join(anagram)

words = ['banana', 'carrots', 'mangoes', 'potatoes']

anagrams = []

# using default for loop
# for word in words:
#   anagrams.append(jumble(word))
# print(anagrams)

# using map function
# anagrams = map(jumble, words)
# print(list(anagrams))

# using comprehension
anagrams = [ jumble(word) for word in words ]
print(anagrams)