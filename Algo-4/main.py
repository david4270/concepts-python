# Probability and Bayes' Theorem

# Ways to arrange r out of n distinct objects when order matters
# P(n,r) = n! / r!
def permutation(n,r):
    if(r == 0):
        return 1
    else:
        return n*permutation(n-1,r-1)

# Ways to arrange r out of n distinct objects when order doesn't matter
# C(n,r) = n! / (r! * (n-r)!)
def combination(n,r):
    return int(permutation(n,r)/factorial(r))

def factorial(a):
    if(a == 0):
        return 1
    elif(a == 1):
        return 1
    else:
        return a*factorial(a-1)

#Probability of OR P(A U B) = P(A) + P(B) - P(A∩B)
def probOr(A,B):
    return A+B-probAnd(A,B)

#Probability of AND P(A∩B) = P(A)*P(B) if A and B independent
def probAnd(A,B):
    return A*B

# Bayes' theorem P(A|B) = P(A∩B)/P(B)
def bayes(A,B):
    return probAnd(A,B)/B

#Coin flip expected value
def coinFlip(nc):
    ev = 0
    for i in range(0,nc+1):
        partialExp = ((3*(nc-i)-2*i)*(1/2**nc)*combination(nc,i))
        print("Expected Value of", i, "tails out of", nc, "coins is", partialExp)
        ev += partialExp
    return ev

def main():
    print("Probability calculation example in independent A and B\n")
    A = 1.1
    B = 1.1
    while(A > 1.0 or B > 1.0):
        print("Probability A: ", end="")
        A = float(input())
        print("Probability B: ", end="")
        B = float(input())
        print(A,B)
        if(A > 1.0 or B > 1.0):
            print("This is impossible. Make input again")
        else:
            print("This is... acceptable. Proceed to probability calculation")
    print("Given that A and B are independent, probability of A or B is: {}".format(probOr(A,B)))
    print("Given that A and B are independent, probability of A and B is: {}".format(probAnd(A,B)))
    print("Given that A and B are independent, conditional Probability of A given B is: {}".format(bayes(A,B)))

    print("\nExpected value example\n")
    print("You will get $3 for head of each coin, and lose $2 for tail of each coin")
    nc = int(input("Insert number of coins: "))
    print("Expected value of flipping", nc, "coins is",coinFlip(nc))

if __name__ == "__main__":
    main()