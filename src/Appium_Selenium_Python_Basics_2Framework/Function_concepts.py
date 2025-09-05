######################  Function Types  ######################
"""
Types of Functions  :  Non-parameter function, parameter function, return type function

--Using "def" allows for creating Functions.
--Function names should be in camel case Ex  :  def yourFunction():
                                                    pass
"""


#   Non-parameter function
def methodOne():
    print("This is Method One")
methodOne()


#   Parameter function
def methodTwo(name):
    print("This is a", name)

methodTwo("Python Tutorial")


#   Return type function
def sumOfTwoNumber(a, b=10):
    c =a+b
    return  c
d = sumOfTwoNumber(10, 5)
print(d)

#   Default value in a function
def sumOfTwoNumber_2(a, b=10):
    c =a+b
    return  c


d = sumOfTwoNumber(10,20)
print(d)



#   Pass list to the function
def listValue(a):
    for x in a:
        print(x)
b =[1,2,3,4,5,6]
listValue(b)



#   Key and value argument
def spkUtterance(request,response,content):
    print("Request :", request)
    print("Response :", response)
    print("Content :", content)
spkUtterance(request="Play :", response="station :", content="Soul")



#   Arbitrary Keyword Arguments, **kwargs
"""

To find keyword arguments passed in a Function add two asterisks ** before the parameter name in the function definition


"""

def spkUtterance(**kwargs):
    print(kwargs)

spkUtterance(request="Play", response="station", content="Soul")


#   Allow a function to pass when executed
def methodThree():
    pass
