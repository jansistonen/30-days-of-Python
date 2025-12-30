for i in range(11):
    print(i)
else:
    print('\n')

i = 0
while i <= 10:
    print(i)
    i += 1

printable = '#'
for i in range(9):
    print(i * printable)

# 4 - Use nested loops to create the following:
'''
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()
    #täällä rivin vaihto?

for i in range(11):
    print(f'{i} x {i} = {i*i}')

'''
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers
'''

list_1 = ['Python', 'Numpy','Pandas','Django', 'Flask']

for element in list_1:
    print(element)

for i in range(101):
    if i % 2 == 0:
        print(i)
    else:
        print(f'  {i}')

sum = 0

for j in range(101):
    sum += j
else:
    print(sum)