#task 1
'''
age = int(input('Enter your age: '))
wait_left = 18 - age
if age < 1818:
    print(f'You need {wait_left} more years to drive')
else:
    print('You are old enough to drive!')
'''

#task 2 - pracitse also forking!!
your_age = int(input('Enter your age: '))
my_age = 31
difference = abs(my_age-your_age)
if difference != 0:
    if difference > 1:
        print(f'We have age difference of {difference} years!')
    else:
        print('We have one year of age difference')
else:
    print('We are same age!!!')

#task 3
a = int(input('inbut a: '))
b = int(input('input b: '))
if a < b:
    print('a is smaller')
elif a > b:
    print('a is bigger')
else:
    print('they are equal')