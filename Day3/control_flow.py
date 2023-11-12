
#height = int(input("what is your hight in cm?"))

# if height >= 120:
#     print("you can ride the elevator")
# else:
#     print("you can not  ride this elevator")


#nested statements = extra conditions

# if height >= 120:
#     print("you can ride the elevator")
#     age = int(input("how old are you?"))
#     if age <=12:
#         print("please pay 5")
#     elif age <18 & age > 12:
#         print("pay 7 dollars")
#     else:
#         print("pay dollars 12")



# else:
#     print("you can not  ride this elevator")


#bmi 2.0 with if else
# height = 1.75
# weight = 70
# bmi = int(weight/(height**2))

# print(bmi)
# if bmi < 18.5:
#   print("they are underweight")
#   print(bmi)
# elif 18.5 < bmi < 25.0:
#   print("they have a normal weight")
#   print(bmi)
# elif bmi >= 25 & bmi < 30:
#   print("they are slightly overveight")
# elif bmi >= 30 & bmi < 35:
#   print("they are obese")
# else:
#   print("they are clinically obese")

#leap year

# This is how you work out whether if a particular year is a leap year.

# on every year that is divisible by 4 with no remainder
    # leap_year % 4 =0 == leap year
# except every year that is evenly divisible by 100 with no remainder
    # leap_year % 2 = 0 == not a leap year
# unless the year is also divisible by 400 with no remainder
    # leap_year % 400 = 0 == is a leap year

# year = 1900

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")


# if a elif b else c = only one of the conditions will be carried out.

#multiple if statements if a if b if c = all conditions are checked


### do you want photo with your ticket.

# height = int(input("whats your hight? "))
# ticket_price = 0

# if height > 120:
#     print("you can ride the elevator")
#     age = int(input("how old are you?"))
#     if age <=12:
#         ticket_price += 5
#         print(f"please pay {ticket_price}")
#     elif age <18 & age > 12:
#         ticket_price += 7
#         print(f"pay {ticket_price} dollars")
#     elif age >18:
#         ticket_price += 12
#         print(f"pay {ticket_price} dollars")
#     answer = input("do you want a photo")
#     if answer == "yes":
#         ticket_price +=3
#         print(f"your ticket is now {ticket_price}")
#     else:
#         print(f"your ticket price is {ticket_price}")
# else:
#     print("no ride for you ")


##### make a pizza order
# small =15
# medium = 20
# large = 25
# pepporony small = 2
# pepporony medium large = 3
# cheese = 1

size = "L"
add_pepperoni = "Y"
extra_cheese ="N"
bill = 0

#& add_pepperoni == "N" & extra_cheese == "N"

if size == "S" :
    bill +=15
    if add_pepperoni == "Y":
        bill +=2
        if add_pepperoni =="N":
              bill+=0
    if extra_cheese == "Y":
        bill +=1
        if extra_cheese == "N":
              bill+=0
    print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {bill}.")
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill +=3
        if add_pepperoni =="N":
              bill+=0
    if extra_cheese == "Y":
        bill +=1
        if extra_cheese == "N":
              bill+=0
    print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {bill}.")
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill +=3
        if add_pepperoni =="N":
              bill+=0
    if extra_cheese == "Y":
        bill +=1
        if extra_cheese == "N":
              bill+=0
    print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {bill}.")

    
   #or 
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

   
    # print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {bill}.")
    # elif add_pepperoni =="Y" & extra_cheese =="N":
    #     bill +=2
    


##
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")




