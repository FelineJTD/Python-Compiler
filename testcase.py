1a = 1
# if (1 == a):
#   print("yes")

from FA import isVarValid
def CNFtoCNFdict(X):
    return 0

def isNotTerminal(X):
    for i in X:
        if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
    return True
import re
# def isString(kata):
    # matched = re.match(r'[\x00-\x7F]*', kata)
    # return bool(matched)
    
# def isNumber(angka):
#     matched = re.match('^[0-9]+$', angka)
#     return bool(matched)

testing = "tes"
testing = 'tes'
regex = '^[0-9]+$'
print(check.y())

# Define a function for
# identifying a Digit
def check(string):
    
     # pass the regular expression
     # and the string in search() method
    if(re.search(regex, string)):
        print("Digit")
         
    else:
        print("Not a Digit")

x = isString("A 123 wlwllw a a")
print(x)
print(check(" "))