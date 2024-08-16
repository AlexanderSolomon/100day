def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True, print("true")
            else:
                return False, print("f")
        else:
            return True , print("true")
    else:
        return False, print("f")
    

is_leap(2000)