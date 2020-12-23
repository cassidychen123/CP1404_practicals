word_calculate = {}  # create a dictionary
text = input("Text: ")  # get word
words = text.split()
for word in words:
    times = word_calculate.get(word, 0)
    word_calculate[word] = times + 1
words = list(word_calculate.keys())
words.sort()
maximum = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, maximum, word_calculate[word]))