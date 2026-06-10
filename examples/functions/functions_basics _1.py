"""
Function Practice Examples
Basic Python function exercises.
"""

def hello ():
    print("Hello World")
hello()


def greet ():
    name = input("What is your name? ")
    print(f"Hello , {name}!")

greet()


def great (name):
    print(f"Hello , {name}!")



def is_positive(num:int):
    if num >= 0:
        return True
    else:
        return False


### def is_positive_2(num:int):
   ###  return num > 0


def is_negative(num:int):
    return not is_positive(num)


def sum_of_squares(num:int, num2:int):
    return num**2 + num2**2


def is_even (num:int):
    if num % 2 == 0:
        return True
    else:
        return False


### def is_even(num:int):
    ###  return num%2 == 0

def is_greater(num:int, num2:int):
    if num > num2:
        return True
    else:
        return False

### def is_greater(num:int, num2:int):
    ### return num > num2

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

### def sum_numbers(*args):
   ### return sum (args)

def pick_evens (*args):
    even = [i for i in args if i % 2 == 0]
    return even

def skyline(*args):
    if  len(args) == 0 :
        return 0
    return max(args)
### return max(args) if args else 0


