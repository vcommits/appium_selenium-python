#   Lists Data Type
"""
Storing various data type values in order and list is changeable in Runtim
Lists allow duplicate values.  Variables/Data Types in Lists are contained in square
brackets "[]"

Ex. shop_cart = [1.7, "subtotal", 1, "state tax", "tax", "tax]
"""

use_list = [7, "thread", 9, 4, 2, 1.4, 3, "gears", "settings"]
print(type(use_list))
print(use_list)


#   Accessing the values in a list listName(indexvalue)
w = use_list[3]
print(w)



#   Slicing - Targeting a specific range of values in a list.
"""
i.e "[0:5]" would slice the FIRST FOUR values in a list as the number
to the right of the colon is the boundary number.  If the target number was
the 5th item in the list then "[0:6]" would be required.  Negative values
read the list from right to left i.e. "[-5]"/
"""

t = use_list[0:6]
print(t)




#   Update the values in a list.
use_list[1] = "stitch"
print(use_list)




#   Append a list.
use_list.append("menu")
print(use_list)



#  Inserting a value into a list (index, "__object")
use_list.insert(3,"10")
print(use_list)



#   Search for a value within a string.
_j = "time" is use_list
print(_j)




#   Iterate the list value
for _j in use_list:
    print(_j)


#   Combine/join/concatentate multiple lists with "+".
A = [9, 8, 7]
B = [6, 5, 4]
C = A + B
print(C)


#   Delete a list.
#del use_list
print(use_list)