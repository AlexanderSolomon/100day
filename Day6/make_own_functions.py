
#when making own function start with keyword def

def myfunction():
    print("hello")
    print("bye")

#call the function by writing the name
myfunction()



# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump_huddle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# huddles = 5
# while huddles > 0:
#     jump_huddle()
#     huddles -=1

# jump_huddle()
# #6 times    

# # challenge 3 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump_huddle():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()



# huddles = 5
# while at_goal() == False:
#     if front_is_clear()== True:
#         move()
#     if wall_in_front() == True:
#         jump_huddle()
#     if at_goal() == True:
#         done()


#challenge 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump_huddle():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# def jump_huddle1():
#     turn_left()
#     while wall_on_right() == True:
#         move()
#     if wall_on_right() == False:
#         turn_right()
#         move()
#         turn_right()
#         while front_is_clear()== True:
#             move()
#         if wall_in_front() and is_facing_north() ==False:
#             turn_left()

# while at_goal() == False:
#     if front_is_clear()== True:
#         move()
#     if wall_in_front() == True:
#         jump_huddle1()
#     if at_goal() == True:
#         done()


# ### Maze challenge
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump_huddle():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# def jump_huddle1():
#     turn_left()
#     while wall_on_right() == True:
#         move()
#     if wall_on_right() == False:
#         turn_right()
#         move()
#         turn_right()
#         while front_is_clear()== True:
#             move()
#         if wall_in_front() and is_facing_north() ==False:
#             turn_left()
        


# # my solution
# while at_goal() == False:
#     if front_is_clear() == True and wall_on_right() == True:
#         move()
#     if front_is_clear() == False and wall_on_right() == True:
#         turn_left()
#         while front_is_clear() == True and wall_on_right() == True:
#             move()
#             if at_goal()== True:
#                 done()
#     if front_is_clear() == False and wall_on_right() == False:
#         turn_right()
#         if front_is_clear() and at_goal()== False:
#             move()
#     if front_is_clear() == True and wall_on_right() == False:
#         turn_right()
#         move()

# ## other solution
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

 