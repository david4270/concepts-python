#basic-7: map, reduced, filter

"""
map() function: https://www.geeksforgeeks.org/python-map-function/?ref=lbp

map(func,iter)

func - function in which map passes each element of given iterable
iter - iterable which is to be mapped
"""

"""
reduce() function: https://www.geeksforgeeks.org/reduce-in-python/?ref=lbp

reduce(func,seq)

Used to apply particular function passed in its argument to all the list elements
"""
import functools
import operator

"""
filter() function: https://www.geeksforgeeks.org/filter-in-python/?ref=lbp

filter(func,seq)

func - function that tests if each element of sequence true or not
seq - sequence which needs to be filtered

returns - iterator that is already filtered
"""


def palindromeFinder(input):
    if(len(input) == 1):
        return True
    elif(len(input) == 2):
        if(input[0] != input[1]):
            return False
        else:
            return True
    else:
        if(input[0] == input[-1]):
            nextTerm = input[1:-1]
            print(nextTerm)
            return palindromeFinder(nextTerm)
        else:
            return False

def main():
    # map() example - palindrome for multiple strings
    print("map() - palindrome example") 
    strInput = ['your','non','topspot']
    returnedBool = map(palindromeFinder,strInput)
    print(list(returnedBool))

    # map() example with lambda - power of integers
    print("map() with lambda - power of integers")
    listNum = [1,2,3,4]
    result = map(lambda x: x**2, listNum)
    print(list(result))

    #reduce() example - add, max, operator.add, operator.mul, 3-element reduce
    li1 = [2,3,5,6,7,4,1,9,8,]
    print("Sum of list elements: ",end="")
    print(functools.reduce(lambda a,b: a+b, li1))
    print("Maximum element: ",end="")
    print(functools.reduce(lambda a,b: a if a>b else b, li1)) 
    print("Sum of list elements using operator.add: ",end="")
    print(functools.reduce(operator.add, li1))
    print("Multiplication of list elements using operator.add: ",end="")
    print(functools.reduce(operator.mul, li1))
    print("Sum of list elements using operator.add and add 13: ",end="")
    print(functools.reduce(operator.add, li1, 13)) 
        #3-element reduce -> 3rd element extends list (but 3rd element cannot be list)
    
    #filter() exmaple with lambda - odd/even number
    result = filter(lambda x: x%2 != 0 , li1)
    print(list(result))
    result = filter(lambda x: x%2 == 0 , li1)
    print(list(result))

    #filter() example - filtering palindromes
    filPalindrome = filter(palindromeFinder,strInput)
    print(list(filPalindrome))



if __name__ == "__main__":
    main()