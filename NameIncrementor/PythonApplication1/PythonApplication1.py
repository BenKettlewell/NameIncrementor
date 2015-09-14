"""
Take input as a long string, for example:

'Systems and Vulns'!D55,'Systems and Vulns'!D56,'Systems and Vulns'!D57,'Systems and Vulns'!D58,'Systems and Vulns'!D59,
'Systems and Vulns'!D60,'Systems and Vulns'!D61,'Systems and Vulns'!D62,'Systems and Vulns'!D63,'Systems and Vulns'!D64,
'Systems and Vulns'!D65,'Systems and Vulns'!D66,'Systems and Vulns'!D67,'Systems and Vulns'!D68,'Systems and Vulns'!D69,
'Systems and Vulns'!D70,'Systems and Vulns'!D71,'Systems and Vulns'!D72,'Systems and Vulns'!D73,'Systems and Vulns'!D74,
'Systems and Vulns'!D75,'Systems and Vulns'!D76,'Systems and Vulns'!D77,'Systems and Vulns'!D78,'Systems and Vulns'!D79

Change the letter after the '!' one further in the alphabet for each item in the comma separated list, and return each one.
"""
import sys
import getopt

def main ():
    ''' EXPLANATION OF PROGRAM
    '''
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(1)
    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere
    
    # Begin Main code    
    listOfExcelStrings = getExcelStrings()
    output = createOutput(listOfExcelStrings);
    printOutput(output)
    

def getExcelStrings():
    ''' NEEDS DOCUMENTATION
    '''
    prompt = "Please enter 2 Excel strings"
    print prompt;
    excelStrings = []
    #for i in range (1,1):
    userProvidedExcelString = raw_input();
    #userProvidedExcelString = "='Systems and Vulns'!B23"
    excelStrings.append(userProvidedExcelString)
    return excelStrings

def createOutput(listOfExcelStrings):
    ''' NEEDS DOCUMENTATION
    '''
    output = []
    output.append(generateNextString(listOfExcelStrings[0]))
    for i in range (0, 20):
        output.append(generateNextString(output[i]))
    return output

def printOutput(output):
    ''' NEEDS DOCUMENTATION
    '''
    for i in range (0, len(output)):
        print output[i]

def generateNextString(previousExcelString):
    ''' NEEDS DOCUMENTATION
    '''
    nextValue = determineNextValue(previousExcelString)
    exclamationIndexes = findAllIndexes (previousExcelString, '!')
    valueIndexes = []
    for i in range(0,len(exclamationIndexes)):
        valueIndexes.append (exclamationIndexes[i]+1)
    newString = list(previousExcelString) # Because Strings are immutable
    for i in valueIndexes:
        newString[i] = nextValue

    return "".join(newString) # Put list back together again

def findAllIndexes(s, ch):
    ''' NEEDS DOCUMENTATION
    '''
    return [i for i, ltr in enumerate(s) if ltr == ch]

def determineNextValue (excelString):
    currentValue = excelString[excelString.index('!') + 1]
    nextValue = chr(ord(currentValue) + 1)
    return nextValue

'''
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
'''
if __name__ == "__main__":
    main()