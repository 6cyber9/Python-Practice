from sys import builtin_module_names


print('David Nwaokolo')
print("o----")
print('  ||||')
print('*' * 10)

print('  ***    ***   ')
print(' *   *  *   *  ')
print('*     **     * ')
print(' *          *  ')
print('  *        *   ')
print('    *    *     ')
print('       *       ')

#Variables
price = 10
price = 20 #Integers
rating = 4.9 #floating
name = 'Mosh' #Strings
is_published = False #Bulean 
print(price)

#Exercise: We check in a patient name John Smith/
# He's 20 years old and is a new patient/
# Create variables.

name = 'John Smith'
age = 20
new_patient = True

#How to insert input from a user 

name = input('What is your name? ') #call input function with ''
color = input ('What is your favourite color? ')
print (name  +  ' likes '  +  color)

#Type Conversion
birth_year = input('Birth year: ') # for integer input functions are in strings and need to be converted to integer via int funtion
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

#ask user weight (in pound) and convert it to Kilogram
user_weight=input('what is your weight in pounds: ')
kilogram_weight = int(user_weight)*0.45
print (kilogram_weight)

#Strings
course1 = 'Python for Beginners'
print(course1)
course2 = 'Python course for "Beginners"'
print(course2)
course3 = "Python's course for Beginners"
print(course3)

#string for email ''' email body'''
email = '''
Hi Mary,

Hope you are doing fine? this is my first email to you

Kind Regards
David Nwaokolo
'''
print(email)

#Index character
course = 'Python for Beginners'
print(course[ : ]) #this index : clone or copy a strin. try [0], [-1], [0:5] etc

course = 'Python for Beginners'
another = course[:]
print(another)

#Guess
name = 'Jennifer'
print(name[1:-1])

#Formated strings 37:38
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder' #string cacatination
print(message)
                 #alternative is the formatted string f''
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a Coder' 
print(msg)

#This program calculates UDL for structures (KN/m^2)
W_in_g=input('What is the total Weight of Member (in gram)? ')
L_in_m=input('What is the Lenght of Member(in meters? ')
B_in_m=input('What is the Breadth of Members(in meters)? ')
F= (float(W_in_g))*10/1000
A= (float(L_in_m))*(float(B_in_m))
print(F/A)

#String Methods 40:53
course = 'Python for Beginners'
print (len(course)) 
#len function can limit character in input field entered by user
print(course.upper())
print(course.lower())
print(course)
print(course.title())
print(course.find('e'))
print(course.replace('Beginners','Absolute Beginners'))
#use 'in' operator to check the existence of a character in a variable
print('Python' in course)
print('python' in course)
#Aritmetic Operations 48:39
print (10 + 3)
print (10 - 3)
print (10 * 3)
print (10 / 3)
print (10 // 3)
print (10 % 3)
print (10 ** 3)

#/augmented assignment operator
x = 10
x += 3 #same as x = x + 3 (increment)
print (x)
x = 10 
x -= 3 #
print(x) #deleting line 14 will output x = ((result of line 13) - 3)

#Operator Precedence (BODMAS) 51:39
x = 10 + 3 * 2
print (x)
x= ( 2 + 3 ) * 10 - 3
print(x)

#Math Functions 55:09
x = 2.9
print(round(x))
print(abs(x))

#import mathematical module for complex maths functions
import math #be mindful of the indentation
print(math.ceil(2.9)) #remember to add print function


#If Statement 58:27

#Writing a program that simulates this quotes below
#If it's hot 
#   It's a hot day
#   Drink plenty of water
#otherwise if it's cold
#    It's a cold day
#    Wear warm clothes
# otherwise 
#    It's a lovely day/

is_hot = False #Change to False and rerun
is_cold= False
if is_hot:# for if it is hot
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day") #this print is not part of the if statement and will not be affected if bulean is False or True



#EXERCISE
#Price of a house is $1M
# If buyer has good credit,
#     they need to put down 10%
# Otherwise
#     they need to put down 20%
# Print the down payment/

#My Solution
house_price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment= float(house_price*10/100)
    print( "Your downpayment is " + str(down_payment))
else:
    down_payment= float(house_price*20/100)
    print( "Your downpayment is " + str(down_payment))#I have problem adding $ sign

#Alternatively Solution by Mosh
price = 1000000
has_good_credit= False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print (f'downpayment is ${down_payment}') #Mosh could add $ sign with his method