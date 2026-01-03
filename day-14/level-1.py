countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use for loop to print each country in the countries list.

for i in countries:
    print(i)

# LEVEL 2
# Use map to create a new list by changing each country to uppercase in the countries list
def to_upper(country):
    return country.upper()

countries_to_upper = map(to_upper, countries)
print(list(countries_to_upper))

names_to_upper = map(to_upper, names)
print(list(names_to_upper))