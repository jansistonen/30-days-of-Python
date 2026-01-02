# 1 - Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(para1, para2):
    sum = para1 + para2
    return sum
print(add_two_numbers(3,4))
print(add_two_numbers(para1=4, para2=60))

# 2 - Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle_area(r):
    area = 3.14 * r**2
    return area
print(circle_area(4))
print(circle_area(r=50))

# 3 - Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#     Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(para1):
    summed = 0
    for i in para1:
        if type(i) == int: #add only if the input is integer
            summed = summed + i
        else:
            print(f'{i} is Not an number!')
    return summed
print(add_all_nums([1,2,3,4,5,6, 'a']))


# 4 - Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
#  Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def cel_to_fah(degree_cel):
    degree_fahr = degree_cel * (9/5) + 32
    return degree_fahr
input_from_user = int(input('Give a temperature in Celcius: '))
print(f'You entered a value of {input_from_user} celcius. That is {cel_to_fah(input_from_user)} in Fahrenheit')
# 5 - Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# 6 - Write a function called calculate_slope which return the slope of a linear equation
# 7 - Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# 8 - Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# 9 - Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).