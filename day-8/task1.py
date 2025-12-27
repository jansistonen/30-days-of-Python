#Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'value1'
dog['color'] = 'value2'
dog['breed'] = 'value3'
dog['legs'] =  'value4'
dog['age'] = 0
print(dog)
#Create a student dictionary and add
#first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first name':'value1',
    'last_name':'value2',
    'gender':'value3',
    'age':'value4',
    'status':'value5',
    'skills':[],
    'country':'value7',
    'city':'value8',
    'address':'value9',
    }
print(student)
#Get the length of the student dictionary
print(len(student))
#Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')))

#Modify the skills values by adding one or two skills
student['skills'] = ['Programming', 'English']
print(student.get('skills'))
#Get the dictionary keys as a list
#Get the dictionary values as a list
#Change the dictionary to a list of tuples using items() method
#Delete one of the items in the dictionary
#Delete one of the dictionaries