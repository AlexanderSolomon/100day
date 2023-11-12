print("welcome to treasure island")
print('''               \||/
                |  @___oo
      /\  /\   / (__,,,,|
     ) /^\) ^\/ _)
     )   /^\/   _)
     )   _ /  / _)
 /\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\
 | \____(      )___) )___
  \______(_______;;; __;;;''')

path_chosen =input("chose L for left or R for right").lower
if path_chosen == "R":
    print("game over looser")
else:
    path_2 = input("you are now by a lake, what will you do S for swim or W for wait by the lake")
    if path_2 == "S":
        print("game over... you got eaten by a shark")
    else:
        path_3 =input("your patience pays off 3 magical doors apear, which will you choose R for red, B for blue or Y for yellow?")
        if path_3 == "B":
            print(" you chose takes you to a very hot and dark place a man with a limb welcomes you(game over)")
        elif path_3 == "R":
            print(" you chose takes you to a very hot and dark place a man with a limb welcomes you(game over)")
        else:
            print( " well done travelor you win")

