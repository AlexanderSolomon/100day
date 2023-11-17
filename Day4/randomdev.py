import random
import my_module

# random_integer = random.randint(1,10)
# print(random_integer)

# print(my_module.pi)

# #create a rondom float between 0 and 1
# random_float = random.random()
# print(random_float)

# #create random float between 0 and 5
# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1,100)
# print(f"your love svore is {love_score}")

# heads_or_tails = random.randint(0,1)
# if heads_or_tails == 0:
#     print("Tails")
# else:
#     print("Heads")


# #lists connections to each other

# states_of_america = ["delaware", "mayland", "maine", "new york"]
# # first value in my list
# print(states_of_america[0])

# states_of_america[1] = "Maryland"
# print(states_of_america[1])

# states_of_america.append("new mexico")
# print(states_of_america)

# states_of_america.extend(["alex","mike","same the wise"])
# print(states_of_america)



names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
names[-1] = "gg" 
names.append("dark_man")
print(names)

print(random.choices(names))

