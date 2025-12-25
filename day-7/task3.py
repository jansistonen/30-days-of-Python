'''Exercises: Level 3
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
 Use the split methods and set to get the unique words.'''

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

set_to_list = list(age)
print(type(set_to_list), set_to_list)

print(len(set_to_list), '\n', len(age))

string = 'I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?'
string_split = string.split(' ')
print(string_split)
string_to_set = set(string_split)
lenght_of_set = len(string_to_set)
print('Lenght of list: ', len(string_split), 'lengths of set: ', lenght_of_set)
print(f'That means there are {lenght_of_set} unique words in a given sentence')