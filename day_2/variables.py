#Day 2: 30 Days of Python programming

#Exercise: Level 1
first_name = 'sakodrake'
last_name = 'toto'
full_name = first_name + ' ' +last_name
country = 'United States of America'
city = 'Columbus'
age = 18
year = 2025
is_married = True
is_true = True
is_light_on = False
skills = ['eating', 'sleeping', 'coding', 'cooking']

#Exercise: Level 2

#1
print(type(first_name))    #str
print(type(last_name))     #str
print(type(full_name))     #str
print(type(country))       #str
print(type(city))          #str
print(type(age))           #int
print(type(year))          #int
print(type(is_married))    #bool
print(type(is_true))       #bool
print(type(is_light_on))   #bool
print(type(skills))        #list
print(len(skills))         #4

#2
print(len(first_name))

#3
print(len(last_name))
print(str(len(first_name)) + ' vs ' + str(len(last_name))) #compare the length of first name and last name

#4
num_one =5
num_two =4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two 
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

#5
#given radius of a circle = 30m, find area, circumference, and take radius as a user input and calculate area
#A = πr^2
#C = 2πr

radius = 30
pi = 3.14
area_of_circle = pi * (radius**2)
circum_of_circle = 2 * pi * radius 
print('Area = ', area_of_circle)
print('Circumference = ', circum_of_circle)

radius_input = input('Enter radius:')
area_of_circle_input = pi * (int(radius_input)**2)
circum_of_circle_input = 2 * pi * int(radius_input)
print('Area = ', area_of_circle_input)
print('Circumference = ', circum_of_circle_input)

#6
first_name_input = input('Enter first name:')
last_name_input = input('Enter last name:')
country_input = input('Enter country:')
age_input = input('Enter age:')

#COMPLETED!!
