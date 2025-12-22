list = list()
list = ['banana','orange','mango','lemon','lime']
print(list)

#task 3
length_of_list = len(list)
print(length_of_list)

#task 4 - Get the first item, the middle item and the last item of the list
first = list[0]
last = list[len(list)-1]
middle_index = int(len(list) / 2)
middle = list[middle_index]

print(first, last, middle)

#task 5 - Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Jan", 31, 174, "In relationship", "Streetname 21"]

#task 6 - Declare a list variable named it_companies and assign initial values 
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Task 7 - print list
print(mixed_data_types)
print(it_companies)
#Task 8
print(len(it_companies))
#Task 9 
first_company = it_companies[0]
last_company = it_companies[-1]
middle_company_index = int(len(it_companies)/2)
middle_company = it_companies[middle_company_index]

print(first_company, last_company, middle_company)