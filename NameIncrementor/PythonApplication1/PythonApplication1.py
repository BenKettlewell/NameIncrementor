"""
Take input as a long string, for example:

'Systems and Vulns'!D55,'Systems and Vulns'!D56,'Systems and Vulns'!D57,'Systems and Vulns'!D58,'Systems and Vulns'!D59,
'Systems and Vulns'!D60,'Systems and Vulns'!D61,'Systems and Vulns'!D62,'Systems and Vulns'!D63,'Systems and Vulns'!D64,
'Systems and Vulns'!D65,'Systems and Vulns'!D66,'Systems and Vulns'!D67,'Systems and Vulns'!D68,'Systems and Vulns'!D69,
'Systems and Vulns'!D70,'Systems and Vulns'!D71,'Systems and Vulns'!D72,'Systems and Vulns'!D73,'Systems and Vulns'!D74,
'Systems and Vulns'!D75,'Systems and Vulns'!D76,'Systems and Vulns'!D77,'Systems and Vulns'!D78,'Systems and Vulns'!D79

Change the letter after the '!' one further in the alphabet for each item in the comma separated list, and return each one.
"""


input = str(input('Paste comma separated list here:'))

input = "'Systems and Vulns'!D55,'Systems and Vulns'!E56,'Systems and Vulns'!F57,'Systems and Vulns'!G58,'Systems and Vulns'!D59"

#Turn comma separated list stored in 'input' into an array
def makeList(input):
    myList = input.split(",")
    return myList

def incrementList(myList, newList):
    #Iterate through myList by popping
    for x in range(len(myList)):
        currentString = myList[x]
        index = currentString.index('!') + 1
        print (currentString[index])
        print (currentString)
        newLetter = chr(ord(currentString[index]) + 1)
        currentString = currentString[:index] + newLetter + currentString[index + 1:]
        print (currentString)
        print ("success")
        newList.append(currentString)

myList = makeList(input)
newList = []
incrementList(myList, newList)

print (myList)
print (newList)
