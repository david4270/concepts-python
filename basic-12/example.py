import re

#regInput = '^[a-z]+' #returns the words which start line and only consist lowercase words
#regInput = '^[a-zA-Z]+' #returns the words which start line and only consist words
#regInput = '^\S+' #returns the words which start line and include any non-whitespace character
#regInput = '[a-zA-Z]+$' #returns the words which end line and only consist words
#regInput = '\S+$' #returns the words which end line and include any non-whitespace character
regInput = 't.*?e' # non-greedy, shortest set of characters (either space or non-space) between t and e 

fileIn = open('big.txt','r')

listOccurences = []
for line in fileIn:
    line = line.strip()
    x = re.findall(regInput, line)
    listOccurences.extend(x)

print(listOccurences)
print("big.txt had {} words that matched {}".format(len(listOccurences), regInput))
