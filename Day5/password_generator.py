import random


letters = ['a','b','c','d','e','f','g','h']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','#','%','&','(',')','+','*']

print("Welcome to the password generator")

nr_letter = int(input("choose how many leters \n"))
nr_numbers = int(input("choose how many numbers \n"))
nr_symbols = int(input("choose how many symbols \n"))



password = ""

for letter in range(1, nr_letter+1):
    random_char = random.choice(letters)
    password = password + random_char
    print(password)
    
for letter in range(1, nr_letter+1):
    random_char = random.choice(letters)
    password = password + random_char
    print(password)

m = (random.sample(letters, nr_letter)) 
n = (random.sample(numbers, nr_numbers))
b = (random.sample(symbols, nr_symbols)) 
print(m)
print(n)
print(b)
simple_code = m + n + b
print(simple_code)
print(*simple_code)
random.shuffle(simple_code) 
hard_code = simple_code
print(*hard_code)
