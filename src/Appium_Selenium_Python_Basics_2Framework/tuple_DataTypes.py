# *************************  Tuple Data Types  *************************
"""
-Tuples are tuple data types are immutable in programming languages like Python. This means that once a tuple is created, its elements cannot be changed, added to, or removed
-values should assign to a variable within parenthesis "()"
 Example :  name_tuple = (1, "python", 2.3, 1)
"""

#   Access the values in a tuple tupleNam[indexValue]
name_tuple = (1, 2, 3, 4, 5, "Python", 1, 2, 3, 4, 5)
a =name_tuple[5]
print(a)


#print(b)
print(name_tuple.count(2))



#   Slicing - Getting the required portion of values within the tuple [1:n-1].
b = name_tuple[4:7]
#   Testing immutability of the tuple (add, insert, remove

#   Length of Tuple - len()
print(len(name_tuple))


#   Getting the count of a Tuple
print(name_tuple.count(1))


#   Locate a value within a Tuple
a = "Python" in name_tuple
print(a)


#   Iterate through a Tuple

for a in name_tuple:
    print(a)


#   Combine Tuples
c = (5, 6, 7, 8)
d = (9, 10, 11, 12)
e =c+d
print(e)



# Delete a Tuple ** This is the desired result.  This will fail at line 52
del name_tuple
print(name_tuple)