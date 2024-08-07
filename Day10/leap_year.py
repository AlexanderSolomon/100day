# Convert the is_leap() functtion
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# Create a new function called days_in_month()
# You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.

# days_in_month(year=2022, month=2)
# And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:

# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.


year= 2020
month= 2
   
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year")
        return True
      else:
        #print("Not leap year")
        return False
    else:
      #print("Leap year")
      return True
  else:
    #print("Not leap year")
    return False
  
print(is_leap(year=year))

# month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
# days_in_month = month_days[month-1]
# print(days_in_month)


# apples = [11,12,13,14] 
# print(apples.index(12))
# print(apples[2])

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year) == True and month == 2:
        print("its a leapyear and 29 days")
        return 29
    else:
        days_in_month = month_days[month-1]
        return days_in_month



#🚨 Do NOT change any of the code below 

days = days_in_month(year,month)
print(days)


