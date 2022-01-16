#Deal with inputs and outputs, with basic data types
#string, list, tuple, set, dictionary, array

"""
string reference: https://www.geeksforgeeks.org/python-strings/?ref=lbp
"""
print("\n\n <<strings>> \n\n")
#string declaration
a = "Glory Glory Tottenham Hotspur \n"
b = "and the Spurs go marching on \n\n"
c = "Tottenham are the greatest team that the world has ever seen \n"
d = "Royal Spurs supports and they come to every game \n"

print(a)
print(b)
print(c)
print(d)

#string concatenation
a = a*3+b
c = c*3+b
d = d*3+b

print(a)
print(c)
print(d)

b = a+c+d
print(b)

#upper case of string
print(b.upper())

#partial string (slicing)
print(a[6:11])
print(a[12:21])

e = "Hello world!"
print(e)
print(e[6:-1])

f = "Say \"Ok Google\" to activate Google Assistant" #escape double quote
print(f)

g = "C:\\Users\\david\\Desktop\\Projects\\Practices\\Concepts-python\\basic-1" #escape backslashes
print(g)

#Formatting string - raw format
h = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58" #Characters in hex format
print(h)
h = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58" #Raw hex format
print(h)

#Formatting string - position
i = "{} {} {} {}".format("Come","On","You","Spurs!")
print(i)

j = "{3} {2} {0} {1}".format("Oh","When","The","Spurs")
print(j)

del e
del f
del g
del h
del i
del j

#Formatting string - type
e = "{0:b}".format(26)
print(e)

e = "{0:e}".format(314.1592)
print(e)

e = "{0:.2f}".format(314.1592)
print(e)

#Formatting string - position]
f = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
print(f)

g = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(g)

del e
del f
del g

"""
list reference: https://www.geeksforgeeks.org/python-list/?ref=lbp
"""
print("\n\n <<lists>> \n\n")
#list declaration and append
e = []
e.append(5)
e.append(7)
e.append("COYS")
e.append(16)
e.append([5,3])
e.append((6,1))
print(e)
print(e[-1])
print(len(e))

#for loop append of list
for i in range(1,4):
    e.append(i)

print(e)

#extending list
f = [5,3,(2,1)]
e.extend(f)

print(e)

del e
del f

#position of multidimension list
e = []
e.append([5,3])
e.extend([[6,7]])
print(e)
print(e[0][0])
print(e[1][1])
print(e[-1][-1])
print(len(e))

e.insert(1,[2,1])
print(e)

e.extend([[1,6],[7,3]])
print(e)

#slicing list
print(e[2:])
print(e[-3:])
print(e[:1])
print(e[:-1])

del e

#list based on equation
odd_sqr = [x ** 2 for x in range(1,11) if x % 2 == 1]
print(odd_sqr)

del odd_sqr

"""
tuple reference: https://www.geeksforgeeks.org/python-tuples/?ref=lbp
"""
print("\n\n <<Tuples>> \n\n")

#declaration of tuples
e = tuple([1,2,3,4,5,6])
f = ("Come","On","You","Spurs")
g = tuple('Tottenham')

print(e)
print(f)
print(g)

#Nested tuple
h=(e,f,g)
print(h)

#Repetition tuple
i = ('COYS',) *3
print(i)

#for loop tuple
j = ('Yeet')
for m in range(int(5)):
    j = (j,)
    print(j)

del e
del f
del g
del h
del i
del j

#Unpacking tuples
e = ("Come","On","You",'Spurs')
f,g,h,i = e
print(e)
print(e[0][0]) #first character of first element of tuple
print(f)
print(g)
print(h)
print(i)

del f,g,h,i

#Concatenation of tuples
f = ("Gunners","Are","The", "Runners")
g = e+f
print(e)
print(f)
print(g)

#slicing of tuples
print(g[4:])
print(g[:4])

#reverse tuple
print(g[::-1])

del e,f,g

"""
set reference: https://www.geeksforgeeks.org/python-sets/?ref=lbp
"""
print("\n\n <<Sets>> \n\n")

#declaration of sets
e = set("Tottenham Hotspur")
print(e)

f = set(["Glory","Glory","Tottenham","Hotspur"])
print(f)

g = set([0,1,2,3,3,3,4,5,6,6,7,7,7,8,9,9])
print(g)

h = set(["Tottenham", "Hotspur", 1882])
print(h)

#add and update set
h.add(2022)
h.add((1961,2008))
h.update([1961,2008])

print(h)

#Accessing elements from set
for i in h:
    print(i, end=" ")

print("\n")

print("Hotspur" in h)

#Removing elements from set
h.remove((1961,2008))
print(h)

h.discard(2022)
print(h)

h.pop() #removes first one
print(h)

#clear set
h.clear()
print(h)

del e,f,g,h

#Frozenset - elements of frozen set remain same after creation
str = ('C','O','Y','S')
e = frozenset(str)
print(e)

del e, str

"""
dictionary reference: https://www.geeksforgeeks.org/python-dictionary/?ref=lbp
"""
#print("\n\n <<Dictionary>> \n\n")




"""
array reference: https://www.geeksforgeeks.org/python-arrays/?ref=lbp
"""
#print("\n\n <<Arrays>> \n\n")




