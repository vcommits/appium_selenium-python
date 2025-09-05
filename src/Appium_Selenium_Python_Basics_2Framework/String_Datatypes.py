# String Data Type Exercises
"""
A Sequence of characters is known as a String
Ex: name = "Python"
"""
from operator import length_hint

#   Assigning Single line string to a variable
_module = "Hello Someone"
print(_module)


#   Assigning Multi line string to a variable
_module2 = """This is a 
              Multi line
              String
              Tackling
              Carriage returns
              & whitespace
              """
print(_module2)

#   Slicing - Extracting the target portion of the data in a string
_module3 = _module[1:3]
_module3 = _module[5:]
print(_module3)


#   String length - len()
print(length_hint(_module2))
print(type(_module2))



#   Change the case sensitivity of a String
print(_module.upper())

print(_module.lower())



#   Replace a portion of a String
print(_module2.replace("Multi","Multiple"))




#   Combining Strings with Concatenation " + "
g = "Linking like...."
h = ".....linking logs"
i = g+h
print(i)


#   Identify elements of a String using Membership Operators - ( in , no in)
#   If the portion of the String is present then "True" will be returned to Terminal.
member = "I'm trying to find this certain brown thing called mulligan"
s = "brown" in member
v = "orange" not in member
t = "pink" in member

print(s, v, t)