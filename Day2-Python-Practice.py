#----------------------------------Day 2------------------------------------------------------------------------------#

#DATATYPES

#STRING
#------------------subscripting------------------------#
-> To pull out a single character from the String
print('HumasUllahJan'[5])
-> To pull out a single character from the reverse of string
print('HumasUllahJan'[-8])

subscripting = input("Enter Word to check 5th character:")
print('Your 5th character is:'+ subscripting[4])

subscripting = input("Enter Word to check 5th character from reverse:")
print('Your 5th character from reverse is:'+ subscripting[-5])
#-----------------------------------------------------------------------------#

print("123" + "456") #-> concatination because it is treated as string
print("123" + '456') #-> concatination because it is treated as string
#------------------------------------------------------------------------------#
#------------------------------Bolean------------------------------------------#
print(True)
print(False)
#-------------------------------------------------------------------------------#

print(len(1234))

print(len(int(1234)))
print(int(len(1234)))
int(print(len(1234)))

integerlength = input('Enter your number to check length')
print(len(integerlength))

integerlength = int(123456789)
print(len(integerlength))
#--------------------------------------------------------------------------------#

#------------------------------------------Type Checking-------------------------#

print(type('String'))
print(type(123))
print(type(123.456))
print(type(True))
print(type(False))
print(type("True"))

#----------------------------------Only print String Why?------------------------------#
datatype = input('Enter Data to the DataType:')
print(type(datatype))

#----------------------------------------------------------------------------------------#

#-----------------------------------Type Casting/Type Conversion-------------------------#
print('123' + '123')
print(int('123'))
print(int('123') + int('123'))
print(str(123) + str(123))
print(str(123))
print(float(123) + float(345))
print(float(123))
print(bool(0))
print(bool(1))
#------------------------------------why it is giving me '2'as an output--------------------------------#
print(bool(123) + bool(234))
#--------------------------------------------------------------------------------------------------------#

#------------------------------------------Making this code Error Free------------------------------------#
print("Number of letters in your Name: " + len(input("Enter your Name: ")))

#----error free-----------------------------------------------#

print("Number of letters in your Name: " + str(len(input("Enter your Name: "))))

#---------------------------------------------------------------------------------------------------------#

#----------------------------------------We cant Concatinate String and Integer Data type-----------------#

print("Number of letters in your Name: " + len(str(input("Enter your Name: "))))
print(str("Number of letters in your Name: " + (len(input("Enter your Name: ")))))
print(str(input('Enter your Name: ')) + len(' '))

name_of_user = (input('Enter your Name\n'))
length_of_name = len(name_of_user)
print(type(name_of_user))
print(type('Number of letters in your name'))
print(type(length_of_name))
print('Number of letters in your name: ' + str(length_of_name))
#-----------------------------------------------------------------------------------------------#

#-------------------------Still this not working-------------------------------------------------#
Phonenumber_of_user = input ("Enter your Phone Number")
Phonenumber_of_user_as_int = int(Phonenumber_of_user)
length_of_phonenumber = len(Phonenumber_of_user)
print(type(Phonenumber_of_user))
print(type('Numbers of integers in your phonenumber'))
print(type(length_of_phonenumber))
print('Numbers of integers in your phonenumber ' + str(length_of_phonenumber))
#-----------------------------------------------------------------------------------------------------#

#-----------------------We cant convert alphabets into string---------------------------------------------#
name_of_user = input('Enter your Name\n')
length_of_name = len(name_of_user)
print(int('Number of letters in your name: ') + length_of_name)
#----------------------------------------------------------------------------------------------------------#

#----------------------------------Mathematical Operations------------------------------------------------#

print(123 + 456)
print(123 - 456)
print(456 - 123)
print(8 * 8)
print(9 / 3)
print(7 // 2) #it ingnores the values after decimal e.g the output is 3.5 and it ignores .5
print(3 ** 3) #it is calculated as power of the Value e.g 3 raise to power 3

#---------------------------------------------------------------------------------------------------------------------------#
#Maths rule -> 'PEMDASLR' -> Pranthases -> exponents -> Multiplication -> Divide -> Addition -> Subtraction -> Left -> Right
#----------------------------------------------------------------------------------------------------------------------------#

print(3*3+3/3-3)
print(3*(3+3)/3-3)
print(4**4+4*4/4-4)

#--------------------------------BMI calculator----------------------------------------------------------------------------#
your_weight = input("Enter your Weight: ")
your_height = input("Enter your Height: ")
weight_as_int = int(your_weight)
height_as_float = float(your_height)
your_BMI = weight_as_int / (height_as_float*0.304)**2
print(your_BMI)

your_weight = input("Enter your Weight: ")
your_height = input("Enter your Height: ")
weight_as_int = int(your_weight)
height_as_float = float(your_height)
your_BMI = weight_as_int / (height_as_float ** 2) # height is in feet so converted to meters
print(your_BMI)
#-----------------------------------------------------------------------------------------------------------------------#

#---------------------------------Flooring---------------------------------------------------#
your_weight = input("Enter your Weight: ")
your_height = input("Enter your Height: ")
weight_as_int = int(your_weight)
height_as_float = float(your_height)
your_BMI = weight_as_int / (height_as_float ** 2) # height is in feet so converted to meters
BMI_as_int = int(your_BMI) #Skiping the digits after Demical
print(BMI_as_int)
#-----------------------------------------------------------------------------------------------#
#------------------------------------Rounding Number-----------------------------------------------#
your_weight = input("Enter your Weight: ")
your_height = input("Enter your Height: ")
weight_as_int = int(your_weight)
height_as_float = float(your_height)
your_BMI = weight_as_int / (height_as_float ** 2) # height is in feet so converted to meters
print(round(your_BMI,3)) #3 represents the number of digits after decimal
#-----------------------------------------------------------------------------------------------------#
#--------------------------------------Assignment Operator--------------------------------------------#

user_score = 0
user_score = user_score +1
print(user_score)
#------------------------------ShortHand---------------------------------------------------------------#
user_score = 3
user_score *=10
print(user_score)

your_current_score = input("Enter your Current Score: ")
score_as_int = int(your_current_score)
score_as_int *=3
print("Score Prediction after 3 Correct Shorts: " + str(score_as_int))
#---------------------------------------------------------------------------------------------------------#
#-------------------------------------------------F-String------------------------------------------------#
your_score = input('Enter your Test Score: ')
your_Age = input('Enter your Age: ')
your_Height = input('Enter your Height: ')
your_selection = True
print(f"Your Test Score is: {your_score}, Your Age is: {your_Age}, Your are Height: {your_Height}, You can be selected: {your_selection}")
#-------------------------------------------------------------------------------------------------------------------#

