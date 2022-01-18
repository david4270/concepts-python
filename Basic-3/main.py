## Recursions

#Fibonacci - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Factorial
def factorial(n):
    if(n == 1):
        ans = 1
    else:
        ans = n*(factorial(n-1))
    print(ans)
    return ans

#Palindrome
def isPalindrome(input):
    if(len(input) == 1):
        return True
    elif(len(input) == 2):
        if(input[0] != input[1]):
            return False
        else:
            return True
    else:
        if(input[0] == input[-1]):
            newinput = input[1:-1]
            print(newinput)
            return isPalindrome(newinput)
        else:
            return False


#Tower of Hanoi
def towerOfHanoi(n, src, dest, temp):
    if(n == 1):
        print("Move",src,"to",dest)
    else:
        towerOfHanoi(n-1, src, temp, dest) #top n-1 from src to temp
        towerOfHanoi(1, src, dest, temp) #move bottm to dest
        towerOfHanoi(n-1, temp, dest, src) #top n-1 from tempt to dest


def main():
    #Factorial
    factorial(6)
    print()
    
    #Palindrome
    input = "topspot"
    print(input)
    if(isPalindrome(input)):
        print(input,"is palindrome")
    else:
        print(input,"is not palindrome")
    print()

    #Fibonacci
    yet = fibonacci(15)
    print(yet)
    print()

    #Tower of Hanoi
    towerOfHanoi(6,'A','B','C')



if __name__ == "__main__":
    main()