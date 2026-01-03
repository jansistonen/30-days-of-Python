#1 - Writ a function which generates a six digit/character random_user_id.  
# print(random_user_id());
#  '1ee33d'

from random import random, randint
import string

def random_user_id(para1):
    id = []
    char_in_use = string.ascii_letters + string.digits
    for i in range(para1):
        id.append(char_in_use[randint(0,len(char_in_use)-1)])
    res = ''.join(id)
    return res
#print(random_user_id())

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but 
# it takes two inputs using input(). One of the inputs is the number of characters and the second input is 
# the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    lenght = int(input('Give a length of an id: '))
    count = int(input("How many id's will be generated: "))

    for i in range(count):
        print('#', random_user_id(lenght))
user_id_gen_by_user()

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    rgb = []
    for i in range(3):
        rgb.append(str(randint(0,255)))
    result = ', '.join(rgb)
    result = 'rgb(' + result + ')'
    return result
print(rgb_color_gen())