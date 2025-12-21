"""a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
per = a+b+c
print("The perimeter of triangle is: ", per)

#task 6
len = int(input("Give length of an rectangle: "))
wid = int(input("Give width of an rectangle: "))

area = len * wid
perimeter = 2*len + 2*wid
print("Area is: ", area, " - Perimeter is: ", perimeter)

#task 7
rad = int(input("Give radius for circle: "))
area = 3.14 * (rad**2)
circumference = 2 * 3.14 * rad
print("Area of a circle is: ", area, " - Circumference is: ", circumference)"""

#task12
a = "Python"
b = "Dragon"
c = len(a)
d = len(b)
print(c," ", d)
print(a == b)

print("on" in a and "on" in b)

#task14

string = "I hope this course is not full of jargon"
word = "jargon"

print("Is the word ", word, " in a sentence? - ", word in string)

#task 16
float_c = float(c)
string_c = str(float_c)
print(float_c, type(float_c), string_c, type(string_c))

#task17
num = int(input("Give a number 0-99: "))
is_even = num % 2
if is_even == 0:
    print("The number is even!")
else:
    print("The number is not EVEN!!")

#task18
