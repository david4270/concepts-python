#Deal with inputs and outputs, with basic data types
#string, list, tuple, set, dictionary, array

"""
string reference: https://www.geeksforgeeks.org/python-strings/?ref=lbp
"""
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






"""
set reference: https://www.geeksforgeeks.org/python-sets/?ref=lbp
"""





"""
dictionary reference: https://www.geeksforgeeks.org/python-dictionary/?ref=lbp
"""





"""
array reference: https://www.geeksforgeeks.org/python-arrays/?ref=lbp
"""





