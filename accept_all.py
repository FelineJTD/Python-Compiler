# A python program to test all keywords below
#here are the keywords
'''
False   class     is      return    None    continue  
for     True      def     from      while   and 
not     with      as      elif      if      or      
else    import    pass    break     in      raise  
'''
from math import sin as alias

# call func
def hello():
    pass

hello()

def read(x):
    with open(x, "r") as f:
        data = "hello"
    if x == 3:
        return data
    elif x == 1:
        return data
    return data
class ExampleClass:
    def function1(parameters):
        continue
    def function2(parameters):
        print(parameters)

class ExPass:
    pass

while True:
    num = 1
    if num == 0:
        raise ZeroDivisionError('cannot divide')
    Var1 = True
    l = [1]
    a = 'testing string var'
    if (1 == 1 and not 1 > 2):
        for i in range(1,10):
            if i == 4:
                continue
            x = None
            print(i)
    elif (Var1 or (False is False)):
        break
    elif (1 in l):
        print("yes")
    else:
        print('This is unreachable')

'''done'''
'''another test for multiline comment
'''
"""
and this one too"""