# modules - seperation of concerns
# order of operations - pemdas - bodmas
# pi = 3.1415
# radius = 5

# area = pi * radius * radius
# print(area)

# radius = 10
# area = pi * radius * radius
# print(area) 

# radius = 12
# area = pi * radius * radius
# print(area)
# user defined functions
# snake case
# Pascal case
# camel case
# parameter / argument - variables

# def area_of_circle(radius):
#     return (pi * radius * radius)

# return and print

def my_power(x, y):
    """this function is for raising x to the power of y"""
    return(x**y)

# def my_append(value,name=[]):
#     name.append(value)
#     return name 
    

# fruits = ['banana','apple']
# print(my_append('grape',fruits))







# collections
# print(dir(list))
# names = []
# # use dot syntax
# names.append('Mandla')
# names.append('Kenias')
# names.append('Takura')
# names.append('Sadson')
# print(f'original: {names}')

# fruits = list('Kenias')
# print(fruits)
# # parts = "This is".split()
# name  = 'Kenias'
# name[0] = 'B'


# name, last = 'Sadson Mk'.split()
# print(name, last)

# ordered  , changeable(mutable), duplicates 

 #unpacking
# print(fruits)

# ordered , unchangeable, duplicates
# reassign the variable
# typecasting



# names = {'Takura','Percy', 'Kenias','Mandla','Sadson'}


# nums1 = {10,20,30,40,5}

# nums2 = {10,20,30,40,50,60}
# nums1.update(names)
# print(help(nums1.isdisjoint))
# print(nums1)

# list,tuple,set,strings 
# dictionaries
# key:value 

# car = { 'name':'mayback','year':2004,'make':'mercedes'}
# x,y = 20,100


# print(car['names'])

# sets and dictionary
# conditionals and loops

# print(dir(car))
# conditionals and loops

# help(dict.fromkeys)
# fruits = ['apple', 'banana', 'Mango','apple','Mango']

# conditionals


# 3 is less than 8  or equal to 8 = True
# loop
# minimize number of operations

name = 'Takura'

# control statements



# homework
# create a program to calculate body mass index(bmi):
# use conditionals
# bmi = weight/height**2
# print(bmi)

# counter = 0
# reserved  word
# hierarchy 

running  = True

# how many times you want to repeat a block of statements

# while running:
#     print(f'The number is {number}')
#     number =  number - 1
#     if number <= 5:
#         break

# for loops
# number = "abcef"

# numbers = set(range(4001))
# new_list = set()


# for x in numbers:
#     if x % 2 != 0:
#      new_list.add(x)

# print(new_list)
# help(print)
# names = ['Percy', "Kenias", 'Takura','Sadson']
# for name in names:
#     pass
n = 11
for x in range(1,n):
    for y in range(1,n):
        print(f"{x*y:3d}", end=' ')
    print()
    

# Number guessing game = loops, variables, conditionals

# introduce git(tool version control) and github(hosting website)
