from random import randint

dice_image = ["1","2","3","4","5","6"]
dice_num = randint(a=1, b=6)
print(dice_image[dice_num])

"""reproduce code so it always has the error out of bounds"""

"""The index out of bounds happens at index 6 of rand int"""
dice_image = ["1","2","3","4","5","6"]
dice_num = randint(a=6, b=6)
print(dice_image[dice_num])


"""correct way to write code would be to set the randint range to 0 and 5 """
dice_image = ["1","2","3","4","5","6"]
dice_num = randint(a=1, b=5)
print(dice_image[dice_num])