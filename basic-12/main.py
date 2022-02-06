#Regex
#https://www.programiz.com/python-programming/regex

import re

def main():
    ##### Introduction to Regex #####
    # https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/?ref=lbp

    # Regex is case sensitive!

    print("Simple regex example")

    coys = "Come on you Spurs"
    print("The given string is:",coys)

    # 'r' stands for raw
    match = re.search(r'Spurs', coys)

    print("Start index:",match.start())
    print("End index:",match.end())
    print()
    
    ### Metacharacters ###
    # \ used to crop special meaning of character following it
    print("Example of \\ in regex")
    s = "Tottenham Hotspur football club was founded in 1882. It is one of the best fooball clubs in the world!"
    print("The given string is:",s)

    match = re.search(r'.',s) # catches first character - T
    print(match)
    match = re.search(r'\.',s) # catches first occurence of .
    print(match)
    print()

    # [] represent character class - set of characters that we wish to match
    print("Example of [] in regex")

    match = re.search(r'[0-2]',s) # matches 0, 1, 2 - matched with 1 in string s
    print(match)

    match = re.search(r'[0,2]',s) # matches 0, 2 - matched with 2 in string s
    print(match)

    match = re.search(r'[^0-2]',s) # matches with characters which are NOT 0, 1, 2 - matched with T in string s
    print(match)

    match = re.search(r'[a-t]',s) # matches lowercase a to t - matched with o in string s
    print(match)
    
    match = re.search(r'[A-C, a-c]',s) # matches lowercase a to c, uppercase A to C - matched with a in string s
    print(match)

    match = re.search(r'[^T, ^H, ^a-z, ^0-9, ^\.]',s) # no uppercase T or H, no lowercase, no number, no . - matched with I in string s
    print(match)
    print()
    
    # ^ matches the beginning
    print("Example of ^ in regex")
    s1 = "Tottenham are the greatest team that the world has ever seen"
    print("The given string is:",s1)

    match = re.search(r'^Totten',s1) # find Totten in the first word (Tottenham)
    print(match)

    match = re.search(r'^Tottenham',s1) # find Tottenham in the first word (Tottenham)
    print(match)
    print()

    # $ matches the end
    print("Example of $ in regex")
    match = re.search(r'en$',s1) # find ending with 'en' in the last word (seen)
    print(match)

    match = re.search(r'ever seen$',s1) # find ending with 'ever seen'
    print(match)
    print()

    # . matches any character except newline
    print("Example of . in regex")

    match = re.search(r'..',s1) # Check first two characters
    print(match)

    match = re.search(r'T.t....',s1) # Check first 7 characters which has T as first and t as third character
    print(match)

    print()

    # | means OR - matches with any of the characters separated by it
    print("Example of | in regex")

    match = re.search(r'a|t|o',s1) # Check first occurence of a,t,o - catches o, which is 2nd character
    print(match)

    match = re.search(r'a|n',s1) # Check first occurence of a,n - catches n, which is 6th character
    print(match)

    print()

    # ? matches zero or one occurrence
    print("Example of ? in regex")

    match = re.search(r'Tot?en',s1) #Tottenham has two t's - returns none
    print(match)

    match = re.search(r'Tot?ten',s1) # Tottenham can be found - t found twice but second t doesn't count in ? - returns Tottenham
    print(match)

    match = re.search(r'gr?e',s1) # 'gre' can be found in greatest - returns gre
    print(match)

    match = re.search(r'se?n',s1) # e repeats twice in seen - returns none
    print(match)

    match = re.search(r'se?en',s1) #seen could be found - only two e's can be found (second e doesn't count in ?) - returns seen
    print(match)
    print()

    # * any number of occurrences (including 0 occurences)
    print("Example of * in regex")
    match = re.search(r'Tot*en',s1) #Tottenham has two t's - returns Totten
    print(match)

    match = re.search(r'Tot*ten',s1) # Tottenham can be found - t found twice but second t doesn't count in * - returns Tottenham
    print(match)

    match = re.search(r'gr*e',s1) # 'gre' can be found in greatest - returns gre
    print(match)

    match = re.search(r'se*n',s1) # e repeats twice in seen - returns seen
    print(match)

    match = re.search(r'se*en',s1) #seen could be found - e found twice (second e doesn't count in *) - returns seen
    print(match)

    match = re.search(r'gra*',s1) # greatest -> a does not occur in 3rd place -> return gr
    print(match)
    print()

    # + one or more occurrences
    print("Example of + in regex")
    match = re.search(r'Tot+en',s1) #Tottenham has two t's - returns Totten
    print(match)

    match = re.search(r'gr+e',s1) # 'gre' can be found in greatest - returns gre
    print(match)

    match = re.search(r'se+n',s1) # e repeats twice in seen - returns seen
    print(match)

    match = re.search(r'gra+',s1) # word with gra- cannot be found - returns none
    print(match)
    print()

    # {} indicate # of occurrences of a preceding regex to match
    print("Example of {} in regex")

    match = re.search(r't{2,3}',s1) # 'Tottenham' has 2 repeated t's - return tt
    print(match)

    match = re.search(r'e{2,3}',s1) # 'seen' has 2 repeated e's - return ee
    print(match)

    match = re.search(r'e{3}',s1) # nothing has eee - return none
    print(match)

    print()

    # () enclose a group of regex
    print("Example of () in regex")
    match = re.search(r'(T|S)o..en.am',s1) # First character T or S, and then as given... return Tottenham
    print(match)

    match = re.search(r'(T|C)o(t+|m)..',s1) # For string 's1' - First character T or C, second characer o, then recurring ts or m, and two characters - return 'Totten'
    print(match)

    match = re.search(r'(T|C)o(t+|m)..',coys) # For string 'coys' - First character T or C, second characer o, then recurring ts or m, and two characters - return 'Come '
    print(match)
    print()

    ### Special Sequences ###
    # \A matches if the string begins with the given character(s)
    print("Example of \\A in regex")

    match = re.search(r'\ACome',coys) #return Come - starts with Come
    print(match)

    match = re.search(r'\ACome',s1) #should return none - starts with Tottenham
    print(match)
    print()

    # \b matches if the word begins/ends with given character(s) - \b(str) check beginning of the word, (str)\b check end of the word
    print("Example of \\b in regex")
    match = re.search(r'\bCo',coys) #return Co - Come starts with Co
    print(match)

    match = re.search(r'me\b',coys) #return me - Come ends with me
    print(match)

    match = re.search(r'urs\b',coys) #return urs - Spurs ends with urs
    print(match)
    print()

    # \B opposite of \b - string should not start/end with given regex
    print("Example of \\B in regex")
    match = re.search(r'\Bome',coys) #return ome - Come does not start with ome
    print(match)

    match = re.search(r'\Burs',coys) #return urs - Spurs does not start with urs
    print(match)
    print()

    # \d matches any decimal digit ([0-9])
    print("Example of \\d in regex")
    match = re.search(r'\d',s) #first digit - return 1
    print(match)

    match = re.search(r'\d+',s) #Longer than one digit - return 1882
    print(match)
    print()

    # \D matches any non digit character ([^0-9])
    print("Example of \\D in regex")


    print()

    # \s matches any whitespace character
    print("Example of \\s in regex")


    print()

    # \S matches any nonwhitespace character
    print("Example of \\S in regex")


    print()

    # \w matches any alphanumeric character ([a-z,A-Z,0-9])
    print("Example of \\w in regex")


    print()

    # \W matches any non-alphanumeric character ([^a-z,^A-Z,^0-9])
    print("Example of \\W in regex")


    print()

    # \Z matches if the string ends with given regex
    print("Example of \\Z in regex")


    print()

    ### Regex module in python ###
    # re.findall() returns all non-overlapping matches of pattern in string, as list of strings

    # re.compile() regular expressions compiled into pattern objects - return list of strings satisfy regex

    # re.split() splits string by occurrences of characters of character or a pattern

    # re.sub() stands for substring - replace substring of string with replacement string, given flag conditions

    # re.subn() - returns tuple with count of total of replacement and string, otherwise same as sub()

    # re.escape() - return string with all non-alphanumerics backslashed

    # re.search() - gives where first occurrence happens
    # start() gives where match starts
    # end() gives where match ends
    # span() gives tuple including start and end
    # group() returns substring where patterns match


    ##### Search, Match, Findall #####
    # https://www.geeksforgeeks.org/regular-expressions-python-set-1-search-match-find/



    ##### search vs findall #####
    # https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/?ref=lbp



    ##### Verbose in Python Regex #####
    # https://www.geeksforgeeks.org/verbose-in-python-regex/?ref=lbp



    ##### Password Validation in Python #####
    # https://www.geeksforgeeks.org/password-validation-in-python/?ref=lbp






if __name__ == "__main__":
    main()
    