# Basic Math in algorithms

# Fibonacci number F_n = F_(n-1) + F_(n-2)
# Check basic-3
from sympy import factor


def fibonacci(a):
    if(a == 0):
        return 0
    elif(a == 1):
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)

# Factorial n! = n*(n-1)*(n-2)* ... *2*1
# Check basic-3
def factorial(a):
    if(a == 0):
        return 1
    elif(a == 1):
        return 1
    else:
        return a*factorial(a-1)

# https://python-course.eu/advanced-python/recursive-functions.php
# Arithmetic series - u_n = a + (n-1)d
class arithmetic:
    def __init__(self, a, d):
        self.a = a
        self.d = d
    
    def term(self, n):
        return self.a + (n - 1) * self.d
    
    def sum(self,n):
        if(n==1):
            return self.a
        else:
            return self.term(n) + self.sum(n-1)


# Geometric series - u_n = a*r^(n-1)
class geometric:
    def __init__(self, a, r):
        self.a = a
        self.r = r
    
    def term(self, n):
        return self.a * (self.r ** (n-1))
    
    def sum(self,n):
        if(n==1):
            return self.a
        else:
            return self.term(n) + self.sum(n-1)


def main():
    m=10
    n=4
    o=5
    aa = 2
    dd = 3
    print("Fibonacci number of",m,"is",fibonacci(m))
    print("Factorial of",n,"is",factorial(n))

    ar = arithmetic(a=aa,d=dd)
    print(str(o)+"th term of arithmetic sequence is",ar.term(o))
    print(str(o)+"th term sum of arithmetic sequence is",ar.sum(o))

    gm = geometric(a=aa,r=dd)
    print(str(o)+"th term of arithmetic sequence is",gm.term(o))
    print(str(o)+"th term sum of arithmetic sequence is",gm.sum(o))

    #infinite sum (a=2, r=0.8) -> infinite sum = a/(1-r) = 2/(1-0.8) = 2/0.25 = 10
    gminf = geometric(a=aa,r=0.8)
    print(gminf.term(100))
    print(gminf.sum(100))


if __name__ == "__main__":
    main()