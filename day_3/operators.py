#Day 3 30 Days of Python Programming

import math

#Exercises

#1
age = 18
height = 6.1
complex = 1 + 1j

#2
# Write a script that prompts the user to enter 
# base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h). 

base_input = input('Enter base:')
height_input = input('Enter height:')
area_of_triangle = 0.5 * int(base_input) * int(height_input)

print(area_of_triangle)

#2
# take inputs and output perimeter of a triangle
sidea_input = input('Enter side A:')
sideb_input = input('Enter side B:')
sidec_input = input('Enter side C:')
perimeter_of_triangle = int(sidea_input) + int(sideb_input) + int(sidec_input)

print(perimeter_of_triangle)

#3
# calculate area and perimeter of a rectangle using prompt of l and w
length = input('Enter length:')
width = input('Enter width')
area_of_rectangle = math.prod(map(int, [length, width]))
perimeter_of_rectangle = sum((2 * int(length), 2 * int(width)))

print('Area of rectangle is: ', area_of_rectangle)
print('Perimeter of rectangle is: ', perimeter_of_rectangle)

#4
# get radius through prompt. calculate area and circumerence where pi = 3.14

radius = input('Enter radius:')
pi = 3.14
area_of_circle = pi * float(radius)**2 
circumference_of_circle = 2 * pi * float(radius)

print('Area of circle: ', area_of_circle)
print('Circumference of circle: ', circumference_of_circle)

#5
# Calculate slope, x-int, and y-int of y= 2x -2
slope = 2
x_int = 1
y_int = -2

#6
# Find slope and Euclidean distance between point (2,2) and point (6,10)

slope2 = (10-2)/(6-2)
Euclidean_distance = ((6-2)**2 + (10-2)**2)**0.5

print('Slope is: ', slope2)
print('Euclidean_distance is: ', Euclidean_distance)

#7
#Compare slopes of #5 and #6
print(slope == slope2)

#8
# Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
a = 1
b = 6
c = 9
discriminant = b**2 - 4*a*c
x1 = (-b + math.sqrt(discriminant)) / (2*a)
x2 = (-b - math.sqrt(discriminant)) / (2*a)

print('Y is 0 at x =', x1, x2)

#9
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('dragon') == len('python'))

#10
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#11
# is jargon in the sentence
print('jargon' in 'I hope this course is not full of jargon.')

#12
# no 'on' in both dragon and python
print(not 'on' in 'dragon' and 'on' in 'python')

#13
# find len of python and convert value to float and convert to string
len_python = len('python')
print(float(len_python))
print(str(len_python))

#14
# check if num is even or not using python
num = input('Input a number:')
if int(num) % 2 == 0:
    print(str(num), ' is even')
else:
    print(num, ' is odd')

#15
# check if // of 7 by 3 is == int(2.7)
print((7//3) == int(2.7))

#16
# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#17
# Check if int('9.8') is equal to 10
# print(int('9.8') == 10) is invalid cause u cant do int of a string
print(int(float('9.8') == 10))

#18
hours_input = input('How many hours are you working?:')
rate_input = input('What is your rate per hour?:')
weekly = int(hours_input) * int(rate_input)

print('Your weekly earning is ', weekly)

#19
# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years_input = input('How many years have you lived so far?:')
print('You have lived for ', int(years_input)*31536000, 'seconds.')

#20
# replicate given table
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')




