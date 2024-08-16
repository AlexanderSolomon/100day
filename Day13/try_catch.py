
#### create a try catch if not int input ####
# age = int(input("how old are you"))
# if age >18 :
#     print(f"you can drive at age {age}")

    
try:
    age = int(input("how old are you"))
except ValueError:
    print("you have tried an invalid number try with a numeriical number example 20")
    age = int(input("how old are you"))
if age >18 :
    print(f"you can drive at age {age}")