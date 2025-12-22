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
#Task 9 - Print the first, middle and last company
first_company = it_companies[0]
last_company = it_companies[-1]
middle_company_index = int(len(it_companies)/2)
middle_company = it_companies[middle_company_index]

print(first_company, last_company, middle_company)

#task 10 - Print the list after modifying one of the companies
it_companies[0] = 'Nokia'
it_companies[-1] = 'Samsung'
print(it_companies)

#Task 11 - Add an IT company to it_companies
it_companies.append('Huawei')
print(it_companies)

 #Task 12 - Insert an IT company in the middle of the companies list
middle_company_index = int(len(it_companies)/2)
it_companies.insert(middle_company_index, 'Canonical')
print(it_companies)

#Task 13
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Task 14 - Join the it_companies with a string '#;  '
result = '#;  '.join(it_companies)
print(result)

#Task 15 - 
print('CGI' in it_companies)

#Task 16 - Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Task 17 - 
it_companies.reverse()
print(it_companies)

#Task 18 & 19
first3 = it_companies[0:3]
last3 = it_companies[-3:]
print(first3, " - ", last3)

#Task 20
mid_index = int(len(it_companies)/2)
if mid_index % 2 == 0:
    mid_comp = it_companies[mid_index:mid_index+1]
else:    
    mid_comp = it_companies[mid_index]
print(mid_comp)

#Task 21
it_companies.pop(0)
print("task21 - ", it_companies)

#Task 22
mid = it_companies[mid_index]
it_companies.pop(mid_index)
print('Popped: ',mid, ' - Left of the list: ', it_companies)

#Task 24
it_companies.clear()
print(it_companies)

#Task 25
del it_companies

#Task 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print(full_stack)