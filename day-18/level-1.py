import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love. '

# What is the most frequent word in the following paragraph?

words = re.findall(r"\w+", paragraph)

#splitted_paragraph = words.split()

#cleaned_paragraph = words = re.findall(r"\w+", sentence)

counter = {}

for word in words:
    word = word.lower()
    '''if word not in counter:
        counter[word] = 1
    else:
        counter[word] = counter[word] + 1'''
    counter[word] = counter.get(word, 0) + 1

print(counter)