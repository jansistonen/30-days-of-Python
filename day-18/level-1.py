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
    counter[word] = counter.get(word, 0) + 1 #.get tarkistaa ensin löydetäänkö annettua paramtria dictionarystä, jos ei, annetaan sille
    #arvo 0

#print(counter)
for key in counter:
    print(key, counter[key])
print('\n---------------\n') #little extrarow for clarity

#haetaan isoin arvo
max_value = -1
max_key = None
temp = []

for k,v in counter.items(): #python specific! you can give key,value - pair to foreach!!
    if v > max_value:
        max_value = v
        max_key = k
    temp.append((v, k)) #lisätään key-value parit listaan mutta arvo ensin! temp on lista jossa elementti on tuple

print(f'Most common word is: {max_key}. It is found {max_value} times!')

temp = sorted(temp, reverse=True) #järjestetään lista jossa on key-value parit, nyt value ensin joten se on järjestysperuste
for i in temp:
    print(i)