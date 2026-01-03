# Exercises: Level 3
#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

from random import randint

def shuffle_list(para1):
    copy_list = list(para1)
    new_list = []
    list_to_set = set(para1)
    for i in range(len(para1)):
        if len(copy_list) > 1:
            index = randint(0,len(copy_list)-1)
            new_list.append(copy_list[index])
            copy_list.remove(copy_list[index])
        else:
            new_list.append(copy_list[0])
    return new_list
print(shuffle_list([7,6,3,5,4,90,12,14,40]))

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.