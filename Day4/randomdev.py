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



# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# names[-2] = "gg" 
# print(names)
# names.append("dark_man")
# print(names)
# names[-1] = "replace dark man"
# print(names)

# print(random.choices(names))


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
#position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position = "B3"

# if position == "A1":
#   line1 = ["X","️⬜️","️⬜️"]
# elif position == "B1":
#   line1 = ["⬜️","X","️⬜️"]
# elif position == "C1":
#   line1 = ["⬜️️","⬜️️","X"]
# elif position == "A2":
#   line2 = ["X","⬜️️","⬜️️"]
# elif position == "B2":
#   line2 = ["⬜️","X","️⬜️"]
# elif position == "C2":
#   line2 = ["⬜️️","⬜️️","X"]
# elif position == "A3":
#   line3 = ["X","️⬜️","️⬜️"]
# elif position == "B3":
#   line3 = ["⬜️","X","️⬜️"]
# elif position == "C3":
#   line3 = ["⬜️️","⬜️️","X"]

#or
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
