#task 1
age = int(input('Enter your age: '))
wait_left = 18 - age
if age < 18:
    print(f'You need {wait_left} more years to drive')
else:
    print('You are old enough to drive!')