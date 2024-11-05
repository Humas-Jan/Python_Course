#----------------------------------------------Day 3-----------------------------------------------------------------------------#

#-----------------------------------------------------Conditional Statments------------------------------------------------------#

#-------------------------------------------Roller-Coster Tickets----------------------------------------------------------------#
print("Welcome to the RollerCoster Ticket Booth!")
your_height = int(input("Enter you Height in Cm's?\n"))
if your_height >= 120:
  print ("Wooo! You can ride take a Roller Coster Ride.")
else:
  print("Ughh! You can't take a Rollar Coster Ride, for Ride you need to Grow Up.")
#------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------Modulo Operator------------------------------------------------------------------------#
number = float(input("Enter Number to divided?:"))
divider = float(input("Enter Divider Number?:"))
result = float(number % divider)
print(f"Your Module is:{result}")

#---------------------------With round Function----------------------------------------------------------#
number = float(input("Enter Number to divided?:"))
divider = float(input("Enter Divider Number?:"))
result = float(number % divider)
print(f"Your Module is:{round(result,2)}")
#-------------------------------------------------------------------------------------------------------------------------------#

print("Enter Number to check Even and  Odd!")
your_number = int(input("Enter your Number?\n"))
calculation = your_number%2
if calculation == 0:
  print("Number you entered is Even")
else:
  print("Number you entered is Odd")
#------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------Nested If/Else Statement--------------------------------------------------------------#
print("Welcome to the RollerCoster Ticket Booth!")
your_height = int(input("Enter your Height in Cm's?\n"))
if your_height >= 120:
  print("Wooo! You can ride take a Roller Coster Ride.")
  your_age = int(input("Enter your Age?\n"))
  if your_age >= 18:
    print("Your ticket will cost 1000 Pkr")
  else: 
    print("your ticket will cost 700 Pkr")
else:
  print("Ughh! You can't take a Rollar Coster Ride, for Ride you need to Grow Up.")

print("Welcome to the RollerCoster Ticket Booth!")
your_height = int(input("Enter your Height in Cm's?\n"))
if your_height >= 120:
  print("Wooo! You can ride take a Roller Coster Ride.")
  your_age = int(input("Enter your Age?\n"))
  if your_age <= 12:
    print("You cant take Ride please Grow up quickly to take Ride:(")
  elif your_age <= 18:
    print("Your ticket will cost 300 Pkr:)")
  elif your_age <= 55:
    print("Your ticket will cost 700 Pkr:)")
  else:  
    print("You cant take Ride it can be Dangerous for you:(")
else:
  print("Ughh! You can't take a Rollar Coster Ride, for Ride you need to Grow Up.")
#---------------------------------------------------------------------------------------------------#
#--------------------------------------BMI Calcultor Succesion---------------------------------------#
weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

print("BMI Calculator!\n")
weight = float(input("Enter your Weight!\n"))
height = float(input("Enter your Height!\n"))
bmi = weight/(height ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

#-------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------If/else statement in Succussion--------------------------------------------------#
#---------------------------------------------------------- I didnt initailize/declared the Bill still working-----------------#
print("Welcome to the RollerCoster Ticket Booth!")
your_height = int(input("Enter your Height in Cm's?\n"))
if your_height >= 120:
  print("Wooo! You can ride take a Roller Coster Ride.")
  your_age = int(input("Enter your Age?\n"))
  if your_age <= 12:
    print("You cant take Ride please Grow up quickly to take Ride:(")
  elif your_age <= 18:
    Bill = 300
    print("Your ticket will cost 300 Pkr:)")
  elif your_age <= 55:
    Bill = 700
    print("Your ticket will cost 700 Pkr:)")
  else:  
    print("You cant take Ride it can be Dangerous for you:(")
  want_photo = input("Do you want to take photo? Write Yes and No.\n")
  if want_photo == "yes":
    Bill += 3
  print(f"Your total Bill is {Bill}")
else:
  print("Ughh! You can't take a Rollar Coster Ride, for Ride you need to Grow Up.")

#----------------------------------------------------------------------------------------------------------------------------#
print("Welcome to the RollerCoster Ticket Booth!")
your_height = int(input("Enter your Height in Cm's?\n"))
if your_height >= 120:
  print("Wooo! You can ride take a Roller Coster Ride.")
  your_age = int(input("Enter your Age?\n"))
  if your_age <= 12:
    Bill = 30
    print("You cant take Ride please Grow up quickly to take Ride:(")
  elif your_age <= 18:
    Bill = 300
    print("Your ticket will cost 300 Pkr:)")
  elif your_age <= 55:
    Bill = 700
    print("Your ticket will cost 700 Pkr:)")
  else: 
    Bill = 30 
    print("You cant take Ride it can be Dangerous for you:(")
  want_photo = input("Do you want to take photo? Write Yes and No.\n")
  if want_photo == "yes":
    Bill += 30
    print(f"Your total Bill is {Bill}")
  if want_photo == "no":
    print("Thank you for coming")
else:
  print("Ughh! You can't take a Rollar Coster Ride, for Ride you need to Grow Up.")
#---------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------Initialize/Declared Bill Variable------------------------------------------#
print("Welcome to the RollerCoster Ticket Booth!")
your_height = int(input("Enter your Height in Cm's?\n"))
Bill = 0
if your_height >= 120:
  print("Wooo! You can ride take a Roller Coster Ride.")
  your_age = int(input("Enter your Age?\n"))
  if your_age <= 12:
    print("You cant take Ride please Grow up quickly to take Ride:(")
  elif your_age <= 18:
    Bill = 300
    print("Your ticket will cost 300 Pkr:)")
  elif your_age <= 55:
    Bill = 700
    print("Your ticket will cost 700 Pkr:)")
  else:  
    print("You cant take Ride it can be Dangerous for you:(")
  want_photo = input("Do you want to take photo? Write Yes and No.\n")
  if want_photo == "yes":
    Bill += 3
  print(f"Your total Bill is {Bill}")
else:
  print("Ughh! You can't take a Rollar Coster Ride, for Ride you need to Grow Up.")
#-----------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------Sum of Two digits using subscripting---------------------------------------#
two_digit_sum = input("Enter Two digits to add \n")
first_digit = int(two_digit_sum[0])
second_digit = int(two_digit_sum[1])
sum = first_digit + second_digit
print(sum)

#-----------------------------------------------------------------------------------------------------------------------------------#

print("Welcome to the Pizza Deliveries!")
want_pizza = input("would you like to order pizza? Yes or No? ")
pizza_size = input("Enter the Pizza Size!\n Small, Medium, Large? : ")
pepperoni = input ("Do you want Pepperoni on your Pizza\n Yes or No? : ")
extra_cheese = input("Do you want Extra cheese on your Pizza \n Yes or No? : ")
if want_pizza == "yes":
    if pizza_size == "small":
        Bill = 3
        if pepperoni == "yes":
            Bill += 1
            print(f"pepperoni added")
        else:
            print(f"No pepperoni added")
    if pizza_size == "medium":
        Bill = 6
        if pepperoni == "yes":
            Bill += 2
            print(f"pepperoni added")
        else:
            print(f"No pepperoni added")
    if pizza_size == "large":
        Bill = 12
        if pepperoni == "yes":
            Bill += 3
            print("pepperoni added")
        else:
            print(f"No pepperoni added")
    if extra_cheese == "yes":
        Bill +=3
        print(f"Extra cheese added \n your bill is {Bill}$")
    else:
        print(f"No extra cheese added \n your Total Bill is {Bill}$")
else:
    print("Thank you for coming!")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

print('Welcome to the Pizza Deliveries!')
want_pizza = input('would you like to order pizza? Yes or No? ')
pizza_size = input('Enter the Pizza Size!\n Small, Medium, Large? : ')
pepperoni = input ('Do you want Pepperoni on your Pizza\n Yes or No? : ')
extra_cheese = input('Do you want Extra cheese on your Pizza \n Yes or No? : ')
if want_pizza == 'yes':
    if pizza_size == 'small':
        Bill = 3
        if pepperoni == 'yes':
            Bill += 1
            print(f'pepperoni added')
        else:
            print(f'No pepperoni added')
    if pizza_size == 'medium':
        Bill = 6
        if pepperoni == 'yes':
            Bill += 2
            print(f'"pepperoni added"')
        else:
            print(f'No pepperoni added')
    if pizza_size == 'large':
        Bill = 12
        if pepperoni == 'yes':
            Bill += 3
            print('pepperoni adde')
        else:
            print(f'No pepperoni added')
    if extra_cheese == 'yes':
        Bill +=3
        print(f'Extra cheese added \n your bill is {Bill}$')
    else:
        print(f'No extra cheese added \n your Total Bill is {Bill}$')
else:
    print('Thank you for coming!')
#---------------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------Logical Operators----------------------------------------------------------#
 
print("Welcome to the RollerCoster Ticket Booth!")
your_height = int(input("Enter your Height in Cm's?\n"))
Bill = 0
if your_height >= 120:
  print("Wooo! You can ride take a Roller Coster Ride.")
  your_age = int(input("Enter your Age?\n"))
  if your_age <= 12:
    print("You cant take Ride please Grow up quickly to take Ride:(")
  elif your_age <= 18:
    Bill = 300
    print("Your ticket will cost 300 Pkr:)")
  elif your_age <= 45:
    Bill = 700
    print("Your ticket will cost 700 Pkr:)")
  elif your_age <= 46 or your_age <= 55:
    Bill = 0
    print("Your are in Mid crisis Life, Your ticket will cost 0 Pkr:)")
  elif your_age >= 56:  
    print("You cant take Ride it can be Dangerous for you:(")
  want_photo = input("Do you want to take photo? Write Yes and No.\n")
  if want_photo == "yes":
    Bill += 3
  print(f"Your total Bill is {Bill}")
else:
  print("Ughh! You can't take a Rollar Coster Ride, for Ride you need to Grow Up.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print("Welcome to the RollerCoster Ticket Booth!")
your_height = int(input("Enter your Height in Cm's?\n"))
Bill = 0
if your_height >= 120:
  print("Wooo! You can ride take a Roller Coster Ride.")
  your_age = int(input("Enter your Age?\n"))
  if your_age <= 12:
    print("You cant take Ride please Grow up quickly to take Ride:(")
  elif your_age <= 18:
    Bill = 300
    print("Your ticket will cost 300 Pkr:)")
  elif your_age <= 45:
    Bill = 700
    print("Your ticket will cost 700 Pkr:)")
  elif your_age >= 46 and your_age <= 55:
    Bill = 0
    print("Your are in Mid crisis Life, Your ticket will cost 0 Pkr:)")
  elif your_age >= 56:  
    print("You cant take Ride it can be Dangerous for you:(")
  want_photo = input("Do you want to take photo? Write Yes and No.\n")
  if want_photo == "yes":
    Bill += 3
  print(f"Your total Bill is {Bill}")
else:
  print("Ughh! You can't take a Rollar Coster Ride, for Ride you need to Grow Up.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

