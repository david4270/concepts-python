#Regex

import re

def main():
    ##### Introduction to Regex #####
    # https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/?ref=lbp

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


    ### Regex module in python ###


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
    