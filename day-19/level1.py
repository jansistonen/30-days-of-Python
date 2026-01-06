import json

# 1 - Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words

f = open('./day-19/obama_speech.txt')

def count_lines(para1):
    lines = f.readlines()
    lines_count = len(lines)
    return lines_count

def count_words(para2):
    f.seek(0) #tämä puuttui aluksi, eli tiedostoa ei luettu koska se on jo luettu aimmmin ja lukukohdistin oli tekstin lopussa, tässä lukukohdistin siirretään alkuun!!!
    lines = f.readlines()
    word_sum = 0
    for i in lines:
        word_sum = word_sum + len(i.split())
    return word_sum



print(count_lines(f), ' riviä puheessa', count_words(f), ' sanaa tekstissä')
f.close()

# 2 - Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages



with open('./day-19/countries-data.json', 'r') as json_file:
    data = json.load(json_file)
    first_country = data[0]
    keys = first_country.keys()

    all_languages = set()

    for country in data:
        all_languages.update(country['languages'])

def most_spoken_languages(countries, count):
    language_count = {}

    for country in countries:
        for language in country['languages']:
            language_count[language] = language_count.get(language, 0) + 1

    #sorttaus
    sorted_languages = sorted(
        language_count.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_languages[:count]

print(most_spoken_languages(data, 3))

def most_population(countries, count):
    result = []
    for country in countries:
        result.append([country['name'], country['population']])
    
    sorted_population = sorted(
        result,
        key = lambda item: item[1],
        reverse=True
    )

    return sorted_population[:count]
print(most_population(data, 10))


        