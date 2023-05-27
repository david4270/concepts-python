import re

regInput = input("Enter a regular expression: ")

fileIn = open('big.txt','r')

listOccurences = []
for line in fileIn:
    line = line.strip()
    x = re.findall(regInput, line)
    listOccurences.extend(x)

print("big.txt had {} words that matched {}".format(len(listOccurences), regInput))
