# a = 1
# if (1 == a):
#   print("yes")

from FA import isVarValid


import re
def isString(kata):
    matched = re.match(r'[\x00-\x7F]*', kata)
    return bool(matched)
    
def isNumber(angka):
    matched = re.match('^[0-9]+$', angka)
    return bool(matched)


regex = '^[0-9]+$'
     
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