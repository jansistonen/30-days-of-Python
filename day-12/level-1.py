#1 - Writ a function which generates a six digit/character random_user_id.  
# print(random_user_id());
#  '1ee33d'

from random import random, randint
import string

def random_user_id():
    id = []
    char_in_use = string.ascii_letters + string.digits
    print(char_in_use)
    for i in range(6):
        id.append(char_in_use[randint(0,len(char_in_use)-1)])
    res = ''.join(id)
    return res
print(random_user_id())

