#Deal with inputs and outputs, with basic data types
#string, list, tuple, set, dictionary, array

#string reference: https://www.geeksforgeeks.org/python-strings/?ref=lbp
a = "Glory Glory Tottenham Hotspur \n"
b = "and the Spurs go marching on \n\n"
c = "Tottenham are the greatest team that the world has ever seen \n"
d = "Royal Spurs supports and they come to every game \n"

print(a)
print(b)
print(c)
print(d)

a = a*3+b
c = c*3+b
d = d*3+b

print(a)
print(c)
print(d)

b = a+c+d
print(b)

print(a[6:11])
print(a[12:21])

e = "Hello world!"
print(e)
print(e[6:-1])

f = "Say \"Ok Google\" to activate Google Assistant" #escape double quote
print(f)

g = "C:\\Users\\david\\Desktop\\Projects\\Practices\\Concepts-python\\basic-1" #escape backslashes
print(g)

h = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58" #Characters in hex format
print(h)
h = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58" #Raw hex format
print(h)

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

e = "{0:b}".format(26)
print(e)

e = "{0:e}".format(314.1592)
print(e)

e = "{0:.2f}".format(314.1592)
print(e)

f = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
print(f)

g = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(g)

del e
del f
del g