#Task 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
strings = ["Thirty", "days", "of","Python"]
print(strings)
full_text = ""
for i in strings:
    full_text += i + " "
print(full_text)

#Task 2 - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
strings2 = ["Coding", "For", "All"]
full_text2 = ""

for i in strings2:
    full_text2 += i + " "
print(full_text2)

#Task 3 - Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#Task 4 - Print the variable company using print().
print(company)

#Task 5 - Print the length of the company string using len() method and print().
print(len(company))

#Task 6 - Change all the characters to uppercase letters using upper() method.
company_upper = company.upper()
print(company_upper)

#Task 7 - Change all the characters to lowercase letters using lower() method.
company_lower = company.lower()
print(company_lower)

#Task 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capitalized = company.capitalize()
title = company.title()
swap = company.swapcase()
print(capitalized, "\n", title, "\n", swap)

#Task 9 - Cut(slice) out the first word of Coding For All string.
print(company[0:6])

#Task 10 - Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding")) #find() returns the index for the word, returns -1 if not found