#build my won calculator
from art import logo
print(logo)
#add function
def add(n1, n2):
    return n1+n2

# subtract function
def sub(n1,n2):
    return n1 - n2

# multiply
def multi(n1,n2):
    return n1 * n2

#divide
def div(n1,n2):
    return n1/ n2


#store function in a dictionary named operations
# # {key: value}
# keys = are the symbols of the functions
# values = are the name of the functions


operations = {"+": add ,"-": sub,"*": multi, "/":div}

def calculater():
    Keep_calculating = True
    #pick number
    num1 = float(input("what is the first number?: "))
    #pick symbol
    for operation in operations:
        print(operation)
    operation_symbol =input("pick 1 symbol: ")
    #pick number 2
    num2 = float(input("what is the second number?: "))
    #find function in dictionary
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    #print answer
    print(f"{num1}{operation_symbol}{num2} = {answer}") 

    while Keep_calculating:
        keep_calc = input("you want to continue press y or n for new calculation")
        if keep_calc.lower() == "y":
            operation_symbol = input("Pick an operation: ") 
            num3 = int(input("What's the next number?: "))

            #Here the calculation_function 
            calculation_function = operations[operation_symbol] 

            #second_answer = multiply(multiply(num1, num2), num3)
            new_answer = calculation_function(answer, num3)
            
            print(f"{answer} {operation_symbol} {num3} = {new_answer}")
            answer = new_answer
        elif keep_calc == "n":
            calculater()
        else:
            Keep_calculating = False

    
calculater()

# if operation_symbol == "+":
#     usercalc = add(n1=num1,n2=num2)
#     print( usercalc) 
# elif operation_symbol == "-":
#     usercalc = sub(n1=num1,n2=num2)
#     print( usercalc)
# elif operation_symbol == "*":
#     usercalc = multi(n1=num1,n2=num2)
#     print( usercalc)
# elif operation_symbol == "/":
#     usercalc = div(n1=num1,n2=num2)
#     print( usercalc)
    

