# Exception Handling
import math

#https://www.geeksforgeeks.org/built-exceptions-python/?ref=lbp
def exp(x):
    try:
        result = math.exp(x)
    except ArithmeticError:
        print("Your input sucks! It OVERFLOWED :(")
        result = 0
    else:
        print("Successful multiplication","exp(",x,")=",result)
    finally:
        return result

def add(x,y):
    try:
        result = x+y
    except ArithmeticError:
        print("Your input sucks! It OVERFLOWED :(")
    else:
        print("Successful addition",x,"+",y,"=",result)
    finally:
        return result

def sub(x,y):
    try:
        result = x-y
    except ArithmeticError:
        print("Your input sucks! It OVERFLOWED :(")
    else:
        print("Successful subtraction",x,"-",y,"=",result)
    finally:
        return result

def mul(x,y):
    try:
        result = x*y
    except ArithmeticError:
        print("Your input sucks! It OVERFLOWED :(")
    else:
        print("Successful multiplication",x,"*",y,"=",result)
    finally:
        return result

#https://www.geeksforgeeks.org/python-try-except/?ref=lbp
def div(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("You are dividing by zero")
        result = 0
    else:
        print("Successful division", x, "/",y,"=",result)
    finally:
        return result


def main():
    add(2,3)
    sub(1,5)
    mul(2,3)
    div(1,3)
    div(2,0)
    exp(3)
    exp(1000)

if __name__ == "__main__":
    main()