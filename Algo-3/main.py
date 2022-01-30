#Permutations and combinations

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
    if(a == 1):
        return 1
    else:
        return a*factorial(a-1)

def main():
    n=10
    r=3
    print("There are", permutation(n,r), "ways to arrange", r, "out of", n, "distinct objects where order is important")
    print("There are", combination(n,r), "ways to arrange", r, "out of", n, "distinct objects where order is not important")


if __name__ == "__main__":
    main()