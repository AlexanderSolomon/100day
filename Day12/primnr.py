# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  
# It should return True or False.

# e.g.
# 7 is a primer number because it is only divisible by 1 and itself.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# NOTE: 1 and 2 are prime numbers because it's only divisible by 1 and itself.


num = 75


def is_prime(num):
    if num == 1 or num == 2:
        return True
    if num > 2:
        if num % 2 == 0 or num % 3 == 0:
            print("False")
            return False
        else:
            print("True")
            return True
        
is_prime(num)