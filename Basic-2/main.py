#Functions practice

#Normal definition of functions
#Global value - https://www.geeksforgeeks.org/global-keyword-in-python/?ref=lbp
#kwargs - https://www.geeksforgeeks.org/args-kwargs-python/?ref=lbps
#yield and generators - https://www.geeksforgeeks.org/generators-in-python/?ref=lbp
#lambda - https://www.geeksforgeeks.org/python-lambda/?ref=lbp
#closure - https://www.geeksforgeeks.org/python-closures/?ref=lbp

# asteval
#https://newville.github.io/asteval/basics.html#creating-and-using-an-asteval-interpreter

from asteval import Interpreter

aeval = Interpreter()

#implemented closures
def integration_kwargs(eqn, **kwargs):
    key_valuelist = {}
    for key,value in kwargs.items():
        key_valuelist[key] = value 
    
    print("Global value delta is",delta)   

    a = key_valuelist['a']
    b = key_valuelist['b']
    n = key_valuelist['n']
    
    def addition():
        sumArea = 0
        for i in range(a*10000,b*10000,int(n*10000)):
            i = i/10000
            flo = eqn.replace('x',str(i))
            fhi = eqn.replace('x',str(i+n))
            flo = aeval(flo)
            fhi = aeval(fhi)
            trapezoidArea = (flo + fhi)*n/2
            sumArea += trapezoidArea
        return sumArea
    
    return addition

def integration(eqn,a,b,n):
    sumArea = 0
    for i in range(a*10000,b*10000,int(n*10000)):
        i = i/10000
        flo = eqn.replace('x',str(i))
        fhi = eqn.replace('x',str(i+n))
        flo = aeval(flo)
        fhi = aeval(fhi)
        trapezoidArea = (flo + fhi)*n/2
        sumArea += trapezoidArea
    print("Global value delta is",delta)
    return sumArea

def integration_yield(eqn,a,b,n):
    #sumArea = 0
    for i in range(a*10000,b*10000,int(n*10000)):
        i = i/10000
        flo = eqn.replace('x',str(i))
        fhi = eqn.replace('x',str(i+n))
        flo = aeval(flo)
        fhi = aeval(fhi)
        trapezoidArea = (flo + fhi)*n/2
        yield trapezoidArea

def simpsonIntegration(eqn,a,b,n):
    sumArea = 0
    s = 0
    for i in range(a*10000,b*10000,int(n*10000)):
        i = i/10000
        flo = eqn.replace('x',str(i))
        fhi = eqn.replace('x',str(i+n))
        flo = aeval(flo)
        fhi = aeval(fhi)
        if (lambda x: x%2 ==0)(s):
            simpsonArea = (n/3)*(flo+2*fhi)
        else:
            simpsonArea = (n/3)*(2*flo+fhi)
        sumArea += simpsonArea
        s+=1
    print("Global value delta is",delta)
    return sumArea

def differentiation(eqn,a,n):
    fa = eqn.replace('x',str(a))
    fhi = eqn.replace('x',str(a+n))
    fa = aeval(fa)
    fhi = aeval(fhi)
    deri = (fhi-fa)/n
    return deri

def main():
    global delta
    n1 = 2
    n2 = 3
    delta = 0.005

    str = "2*x**3+3*x**2"

    integral = integration(str,n1,n2,delta)
    integral_kwargs = integration_kwargs(str, a = n1, b = n2, n = delta)
    simpsonintegral = simpsonIntegration(str,n1,n2,delta)
    derivative = differentiation(str,n1,delta)

    print("Integration using trapezoidal rule:",integral)
    print("Integration using trapezoidal rule (kwargs):",integral_kwargs())
    print("Integration using Simpson's rule:",simpsonintegral)
    print("Derivative:", derivative)

    yld = integration_yield(str,n1,n2,delta)
    
    if((n2-n1)/delta > 5):
        print("\n\nFirst five partial integrals are: ")
        print(yld.__next__())
        print(yld.__next__())
        print(yld.__next__())
        print(yld.__next__())
        print(yld.__next__())


if __name__ == "__main__":
    main()

# NOT covered - first class functions/decorators/memoization?
