countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use for loop to print each country in the countries list.

for i in countries:
    print(i)

# LEVEL 2
# 1 - Use map to create a new list by changing each country to uppercase in the countries list
def to_upper(country):
    return country.upper()

countries_to_upper = map(to_upper, countries)
print(list(countries_to_upper))

# 2 - Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def f(number):
    return number * number
square_numbers = map(f, numbers)
print(list(square_numbers))

# 3 - Use map to change each name to uppercase in the names list

names_to_upper = map(to_upper, names)
print(list(names_to_upper))

# 4 - Use filter to filter out countries containing 'land'.
def y(country):
    if 'land' in country:
        return True
    else:
        return False
land_countries = filter(y, countries)
print(list(land_countries)) # should print only countries that include 'land'

# 5 - Use filter to filter out countries having exactly six characters.
def is_six(country):
    if len(country) == 6:
        return True
    else:
        return False
countries_of_len = filter(is_six, countries)
print(list(countries_of_len))